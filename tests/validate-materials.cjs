#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');

const root = path.resolve(__dirname, '..');
const context = {window: {}, document: {readyState: 'loading', addEventListener() {}}};
vm.createContext(context);
for (const filename of ['curriculum.js', 'materials.js', 'materials-a1-calibration.js', 'material-engine.js']) {
  vm.runInContext(fs.readFileSync(path.join(root, filename), 'utf8'), context, {filename});
}

const curriculum = context.window.RSL_CURRICULUM;
const engine = context.window.RSL_MATERIAL_ENGINE;
const a1 = context.window.RSL_A1_CALIBRATION;
const expectedNoteIDs = ['A1-DL-004','A1-PR-001','A1-PR-005','A1-FS-001','A1-BE-001','A1-NE-003','A1-NE-004','A1-SI-001','A1-TO-001'];
const errors = [];
function check(ok, message) { if (!ok) errors.push(message); }

check(Array.isArray(a1) && a1.length === 50, 'Calibration corpus must contain exactly 50 A1 sentences');
const ids = new Set();
const rus = new Set();
const categoryCounts = Object.fromEntries(curriculum.categories.map(c => [c.code, 0]));
for (const entry of a1) {
  check(/^A1-[A-Z]{2}-\d{3}$/.test(entry.id), 'Invalid ID: ' + entry.id);
  check(!ids.has(entry.id), 'Duplicate ID: ' + entry.id);
  ids.add(entry.id);
  check(entry.level === 'A1', 'Wrong level: ' + entry.id);
  check(Object.hasOwn(categoryCounts, entry.category), 'Unknown category: ' + entry.id);
  if (Object.hasOwn(categoryCounts, entry.category)) categoryCounts[entry.category]++;
  for (const field of ['ru', 'jp', 'en', 'scene']) {
    check(typeof entry[field] === 'string' && entry[field].trim().length > 0, 'Missing ' + field + ': ' + entry.id);
  }
  check(!rus.has(entry.ru), 'Duplicate Russian sentence: ' + entry.id);
  rus.add(entry.ru);
  check(Array.isArray(entry.chunks) && entry.chunks.length > 0, 'Missing chunks: ' + entry.id);
  if (Array.isArray(entry.chunks)) {
    const clean = text => text.replace(/[.,!?—:;«»“”]/g, '').replace(/\s+/g, ' ').trim();
    check(clean(entry.chunks.join(' ')) === clean(entry.ru), 'Chunk coverage mismatch: ' + entry.id);
  }
  if (entry.anatomyFocus) {
    check(entry.anatomyFocus.parts.join('') === entry.anatomyFocus.word, 'Anatomy does not reconstruct word: ' + entry.id);
  }
}
for (const [cat, count] of Object.entries(categoryCounts)) check(count === 5, cat + ' has ' + count + ' items; expected 5');
for (const id of expectedNoteIDs) check(typeof a1.find(x => x.id === id)?.pedagogicalNote === 'string', 'Missing pedagogical note: ' + id);
check(a1.find(x => x.id === 'A1-CE-005')?.ru === 'Сегодня мы идём в музей.', 'CE-005 word order regression');
check(a1.find(x => x.id === 'A1-SI-004')?.jp === '今日はインターネットがつながりません。', 'SI-004 translation regression');
check(engine.getByLevel('A1').length === 50, 'Material Engine A1 count mismatch');
check(engine.getById('A1-BE-001')?.pedagogicalNote?.includes('устала'), 'Material Engine loses pedagogical note');
check(engine.getByLevel('UNCLASSIFIED').length > 0, 'Legacy materials are missing');
check(engine.getAll().every(x => x.id && x.ru), 'Material Engine emitted invalid entry');

if (errors.length) {
  for (const error of errors) process.stderr.write('FAIL ' + error + '\n');
  process.exitCode = 1;
} else {
  process.stdout.write('PASS: 50 A1 sentences, 10 × 5 categories, stable IDs, unique text, chunks, notes, anatomy and Material Engine.\n');
}
