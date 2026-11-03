# Generic geospatial validation checklist

## Inventory and provenance
- Identify authoritative source, owner, license, version, checksums and lineage when available.
## Source
- Validate file readability, completeness, schema and types.
- Validate CRS, axis order, geometry/grid, spatial extent and precision.
- Check nulls/nodata, duplicates, ranges and referential integrity where applicable.
- Validate temporal fields and metadata only where applicable.
## Transformation
- Verify expected CRS/extent, feature counts or cell dimensions, nodata, units and geometry preservation as appropriate.
- Compare samples with approved tolerances and transformation semantics.
## Publication
- Validate accessible download or service, metadata, declared CRS and extent, output schema, format decoding and content completeness.
- For APIs, check relevant protocol conformance, filtering, pagination and error responses.
## Independent consumption
- Decode using an independent client and compare representative delivered samples to authoritative data.
- Test boundaries and exceptional geometry when applicable.
## Report
- Record command/query, software versions, timestamps, sample coverage, status, evidence, limitations and reviewer.
