<p align="center">
  <img src="profile/guard_core_logo_512.png" width="180" alt="Guard Core logo"/>
</p>

# Guard Core

Open-source, framework-agnostic API security: one detection engine, thin adapters for the framework you already run.

The engine sits **in-process** - no proxy, no edge box - detecting and blocking injection, XSS, bot and behavioral attack patterns where your code runs. Self-hosted by design and **GDPR compliant**: telemetry is opt-in and nothing leaves your deployment.

## Engines and adapters

| Language | Engine | Adapters |
|---|---|---|
| Python | [guard-core](https://github.com/Guard-Core/guard-core) | [fastapi-guard](https://github.com/Guard-Core/fastapi-guard) - [flaskapi-guard](https://github.com/Guard-Core/flaskapi-guard) - [djapi-guard](https://github.com/Guard-Core/djapi-guard) - [tornadoapi-guard](https://github.com/Guard-Core/tornadoapi-guard) |
| TypeScript | [guard-core-ts](https://github.com/rennf93/guard-core-ts) | express, fastify, nestjs and hono adapters ship inside guard-core-ts |
| Rust | [guard-core-rs](https://github.com/rennf93/guard-core-rs) | [axum-guard-rs](https://github.com/rennf93/axum-guard-rs) - [actix-guard-rs](https://github.com/rennf93/actix-guard-rs) - [rocket-guard-rs](https://github.com/rennf93/rocket-guard-rs) - [tower-guard-rs](https://github.com/rennf93/tower-guard-rs) |
| Go | [guard-core-go](https://github.com/rennf93/guard-core-go) | [gin-guard](https://github.com/rennf93/gin-guard) - [fiber-guard](https://github.com/rennf93/fiber-guard) - [echo-guard](https://github.com/rennf93/echo-guard) - [nethttp-guard](https://github.com/rennf93/nethttp-guard) - [prest-guard](https://github.com/rennf93/prest-guard) |
| PHP | [guard-core-php](https://github.com/rennf93/guard-core-php) | [laravel-guard](https://github.com/rennf93/laravel-guard) - [slim-guard](https://github.com/rennf93/slim-guard) - [symfony-guard](https://github.com/rennf93/symfony-guard) - [psr15-guard](https://github.com/rennf93/psr15-guard) |

## Telemetry agents

[guard-agent](https://github.com/Guard-Core/guard-agent) (Python) - [guard-agent-ts](https://github.com/rennf93/guard-agent-ts) - [guard-agent-rs](https://github.com/rennf93/guard-agent-rs) - [guard-agent-go](https://github.com/rennf93/guard-agent-go) - [guard-agent-php](https://github.com/rennf93/guard-agent-php)

## Tooling

- [guard-core-mcp](https://github.com/Guard-Core/guard-core-mcp): an MCP server that answers Guard questions from the libraries installed in your interpreter
- [saas-issues](https://github.com/Guard-Core/saas-issues): public issue tracker for the Guard Core SaaS

## Links

- Website: https://guard-core.com
- Playground: https://playground.guard-core.com
- SaaS app: https://app.guard-core.com

## Status

The Python family is the reference implementation and ships from this org. The TypeScript, Rust, Go and PHP families are developed in the open and join this org as they reach parity.
