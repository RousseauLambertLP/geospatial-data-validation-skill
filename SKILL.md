---
name: geospatial-data-publication-validation
description: Vendor-neutral, domain-neutral validation of geospatial datasets from authoritative sources through transformations to public downloads and services, with reproducible evidence and human release approval.
---

# Geospatial Data Publication Validation

## Scope
Validate vector, raster, multidimensional, point-cloud and tabular geospatial datasets across source, transformation, publication and client consumption. Apply only relevant checks; never presume a format, domain, service, or tool. Work with local files, object storage, databases, downloads and OGC services when access is available.

## Required context
Discover or request: dataset identifier, authoritative source, target publication channel, declared coordinate reference system (CRS), expected geographic/temporal extent, transformation lineage, applicable metadata standard, quality requirements and tolerance thresholds. If unavailable, mark the affected checks NOT_TESTED. Never invent acceptance thresholds.

## Procedure
1. Read `references/policy.md`, `references/checklist.md` and the applicable dataset profile. Without an approved profile, run exploratory checks only and mark release decision NEEDS_REVIEW.
2. Inventory inputs and outputs: format, size, checksums if supplied, schema, fields/bands, types, geometry, CRS, extent, resolution, time dimensions, nodata and provenance as applicable.
3. Validate source integrity and structure: parseability, expected schema, geometry validity, topology where relevant, raster grid and pixel semantics, coordinate ordering, missing values, metadata consistency and attribute constraints.
4. Validate transformations against documented intent: reprojection, clipping, filtering, simplification, aggregation, resampling, interpolation, unit conversion, encoding and nodata behavior. Use representative samples and appropriate comparison metrics; do not require exact equality where transformation changes values legitimately.
5. Validate public delivery: discoverability, accessibility, declared metadata, download integrity, service conformance when relevant, CRS, bounding box, pagination, filtering, formats, error handling and freshness where specified. HTTP success alone does not prove data correctness.
6. Independently read delivered outputs and compare against authoritative sources at representative locations/features, boundaries and relevant edge cases (including dateline/poles only when applicable). Document sampling strategy and uncertainties.
7. Produce a report using `references/report-template.md`: per-check PASS / WARN / FAIL / NOT_TESTED / NOT_APPLICABLE, evidence, observed/expected, severity, and release recommendation.
8. Escalate blocking failures for human review. Do not publish, mutate authoritative datasets, or approve release autonomously.

## Execution rules
- Deterministic tests and documented thresholds decide compliance; LLM reasoning explains findings but is not itself evidence.
- Default to read-only checks and bounded sampling. Never expose credentials or confidential endpoints.
- If tools, network access, source data or baselines are missing, explicitly state the validation coverage gap.
- A passing subset of checks is not an end-to-end PASS.
- Use `scripts/check_raster.py` only when GDAL is installed and the input is a compatible raster. Other formats require appropriate tools; absence of a script is not a failure.
- Dataset-specific rules belong in `profiles/`, not this skill. Profiles are examples until reviewed and approved by the data owner.
