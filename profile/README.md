<p align="center">
  <img src="../profile/guard_core_legend_1200x630.svg" alt="Guard Core logo"/>
</p>

Open-source, framework-agnostic API security: one detection engine, thin adapters for the framework you already run.

The engine sits **in-process** - no proxy, no edge box - detecting and blocking injection, XSS, bot and behavioral attack patterns where your code runs. Self-hosted by design and **GDPR compliant**: telemetry is opt-in and nothing leaves your deployment.

## Engines and adapters

| Language | Engine | Adapters |
|---|---|---|
| Python | [guard-core](https://github.com/Guard-Core/guard-core) | [fastapi-guard](https://github.com/Guard-Core/fastapi-guard) - [flaskapi-guard](https://github.com/Guard-Core/flaskapi-guard) - [djapi-guard](https://github.com/Guard-Core/djapi-guard) - [tornadoapi-guard](https://github.com/Guard-Core/tornadoapi-guard) |
| TypeScript | [guard-core-ts](https://github.com/Guard-Core/guard-core-ts) | [express](https://github.com/Guard-Core/guard-core-ts/tree/master/packages/express) - [fastify](https://github.com/Guard-Core/guard-core-ts/tree/master/packages/fastify) - [nestjs](https://github.com/Guard-Core/guard-core-ts/tree/master/packages/nestjs) - [hono](https://github.com/Guard-Core/guard-core-ts/tree/master/packages/hono) |
| Rust | [guard-core-rs](https://github.com/Guard-Core/guard-core-rs) | [axum-guard-rs](https://github.com/Guard-Core/axum-guard-rs) - [actix-guard-rs](https://github.com/Guard-Core/actix-guard-rs) - [rocket-guard-rs](https://github.com/Guard-Core/rocket-guard-rs) - [tower-guard-rs](https://github.com/Guard-Core/tower-guard-rs) |
| Go | [guard-core-go](https://github.com/Guard-Core/guard-core-go) | [gin-guard](https://github.com/Guard-Core/gin-guard) - [fiber-guard](https://github.com/Guard-Core/fiber-guard) - [echo-guard](https://github.com/Guard-Core/echo-guard) - [nethttp-guard](https://github.com/Guard-Core/nethttp-guard) - [prest-guard](https://github.com/Guard-Core/prest-guard) |
| PHP | [guard-core-php](https://github.com/Guard-Core/guard-core-php) | [laravel-guard](https://github.com/Guard-Core/laravel-guard) - [slim-guard](https://github.com/Guard-Core/slim-guard) - [symfony-guard](https://github.com/Guard-Core/symfony-guard) - [psr15-guard](https://github.com/Guard-Core/psr15-guard) |
| JVM (Kotlin, Java) | [guard-core-jvm](https://github.com/Guard-Core/guard-core-jvm) | [spring-boot-guard](https://github.com/Guard-Core/spring-boot-guard) - [ktor-guard](https://github.com/Guard-Core/ktor-guard) |

## Telemetry agents

[guard-agent](https://github.com/Guard-Core/guard-agent) (Python) - [guard-agent-ts](https://github.com/Guard-Core/guard-agent-ts) - [guard-agent-rs](https://github.com/Guard-Core/guard-agent-rs) - [guard-agent-go](https://github.com/Guard-Core/guard-agent-go) - [guard-agent-php](https://github.com/Guard-Core/guard-agent-php) - [guard-agent-jvm](https://github.com/Guard-Core/guard-agent-jvm)

## Tooling

- [Guard-Core-MCP](https://github.com/Guard-Core/guard-core-mcp): an MCP server that answers Guard questions from the libraries installed in your interpreter
- [SaaS Issues](https://github.com/Guard-Core/saas-issues): public issue tracker for the Guard Core SaaS

## Links

- Website: https://guard-core.com
- Playground: https://playground.guard-core.com
- SaaS app: https://app.guard-core.com

## Status

Every family lives in this org. The Python family is the reference implementation, and the TypeScript, Rust, Go, PHP and JVM engines run its conformance fixtures in CI. Engines release together under one version, and so do the agents; adapters version on their own because they track their frameworks.
