# Guard Core

Open-source, framework-agnostic API security: one detection engine, thin adapters for the framework you already run.

The engine sits **in-process** - no proxy, no edge box - and detects and blocks injection, XSS, bot and behavioral attack patterns where your code runs. Self-hosted by design and GDPR-friendly: telemetry is opt-in and nothing leaves your deployment.

## The ecosystem

| Language | Engine / adapters | Agent |
|---|---|---|
| Python | [guard-core](https://github.com/Guard-Core/guard-core) - [fastapi-guard](https://github.com/Guard-Core/fastapi-guard) - [flaskapi-guard](https://github.com/Guard-Core/flaskapi-guard) - [djapi-guard](https://github.com/Guard-Core/djapi-guard) - [tornadoapi-guard](https://github.com/Guard-Core/tornadoapi-guard) | [guard-agent](https://github.com/Guard-Core/guard-agent) |
| TypeScript | [guard-core-ts](https://github.com/rennf93/guard-core-ts) (express, fastify, nestjs, hono) | guard-agent-ts |
| Rust | guard-core-rs (actix, axum, rocket, tower) | guard-agent-rs |
| Go | guard-core-go (gin, fiber, echo, nethttp, prest) | guard-agent-go |
| PHP | guard-core-php (laravel, slim, symfony, psr15) | guard-agent-php |

Also here: [guard-core-mcp](https://github.com/Guard-Core/guard-core-mcp) (an MCP server that answers Guard questions from the libraries installed in your interpreter) and [guard-core-app](https://github.com/Guard-Core/guard-core-app) (the hosted platform: dashboards, threat aggregation, alerting).

## Links

- Website: https://guard-core.com
- Playground: https://playground.guard-core.com
- API: https://api.guard-core.com

## Status

The Python family is the reference implementation and ships from this org. The TypeScript, Rust, Go and PHP families are developed in the open and will move here as they reach parity.
