# CHANGELOG

## UNRELEASED

- Added support for `Upload` scalar. Added support for file uploads to `AsyncBaseClient` and `BaseClient`.
- Added validation of defined operations against the schema.
- Removed `mixin` directive from fragment string included in operation string sent to server.
- Added support for `mixin` directive on fragments definitions.
- Added support for fragments defined on subtype of field's type.
- Added default representation for a field name consisting only of underscores.
- Changed generated client and models to use pydantic v2.


## 0.7.1 (2023-06-06)

- Fixed `AsyncBaseClient` and `BaseClient` to send `Content-Type` header with requests.


## 0.7.0 (2023-06-01)

- Added support for subscriptions as async generators.
- Changed how fragments are handled to generate separate module with fragments as mixins.
- Fixed `ResultTypesGenerator` to trigger `generate_result_class` for each result model.
- Changed processing of models fields to trim leading underscores.
- Added `ShorterResultsPlugin` to standard plugins.
- Fixed handling of inline fragments inside other fragments.
- Changed generated unions to use pydantic's discriminated unions feature.
- Replaced HTTPX's `json=` serializer for query payloads with pydantic's `pydantic_encoder`.
- Removed `mixin` directive from operation string sent to server.
- Fixed `ShorterResultsPlugin` that generated faulty code for discriminated unions.
- Changed generator to ignore unused fragments which should be unpacked in queries.
- Changed type hints for parse and serialize methods of scalars to `typing.Any`.
- Added `process_schema` plugin hook.


## 0.6.0 (2023-04-18)

- Changed logic how custom scalar imports are generated. Deprecated `import_` key.
- Added escaping of GraphQL names which are Python keywords by appending `_` to them.
- Fixed parsing of list variables.
- Changed base clients to remove unset arguments and input fields from variables payload.
- Added `process_name` plugin hook.


## 0.5.0 (2023-04-05)

- Added generation of GraphQL schema's Python representation.
- Fixed annotations for lists.
- Fixed support of custom operation types names.
- Unlocked versions of black, isort, autoflake and dev dependencies
- Added `remote_schema_verify_ssl` option.
- Changed how default values for inputs are generated to handle potential cycles.
- Fixed `BaseModel` incorrectly calling `parse` and `serialize` methods on entire list instead of its items for `List[Scalar]`.


## 0.4.0 (2023-03-20)

- Fixed generating models from interfaces with inline fragments.
- Added default `None` values for generated methods optional arguments.
- Added basic plugin system.
- Added `InitFileGenerator`, `EnumsGenerator`, `ClientGenerator` and `ArgumentsGenerator` plugin hooks.
- Added `InputTypesGenerator` and `ResultTypesGenerator` plugin hooks.
- Added `ScalarsDefinitionsGenerator` and `PackageGenerator` plugin hooks.
- Added support for `[tool.ariadne-codegen]` section key. Deprecated `[ariadne-codegen]`.
- Added support for environment variables to remote schema headers values.
- Added `--config` argument to `ariadne-codegen` script, to support reading configuration from custom path.


## 0.3.0 (2023-02-21)

- Changed generated code to pass `mypy --strict`.
- Changed base clients to get full url from user.
- Added support for custom scalars.


## 0.2.1 (2023-02-13)

- Fixed incorrectly raised exception when using custom scalar as query argument type.


## 0.2.0 (2023-02-02)

- Added `remote_schema_url` and `remote_schema_headers` settings to support reading remote schemas.
- Added `headers` argument to `__init__` methods of `BaseClient` and `AsyncBaseClient`.
