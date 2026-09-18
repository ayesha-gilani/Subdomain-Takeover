# Detection Rule Test Results

## Test Objective

The detection rule was tested against two authorized lab log samples:
one representing possible subdomain takeover exposure and one
representing normal third-party hosting.

## Test 1 — Suspicious Sample

Input:
`attack_sample.log`

Expected Result:
Alert should be generated.

Actual Result:
Alert generated for Possible Subdomain Takeover Exposure.

Status:
PASS

## Test 2 — Benign Sample

Input:
`benign_sample.log`

Expected Result:
No alert should be generated.

Actual Result:
No alert generated.

Status:
PASS

## Summary

The detection logic successfully identified the suspicious sample
while ignoring the benign sample.

This test demonstrates basic detection coverage and false-positive
reduction against the two available lab scenarios.