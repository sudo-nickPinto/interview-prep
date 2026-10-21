# System Design

## What the interview is

You're given a vague prompt like *"Design a URL shortener"* or *"Design Instagram's feed"* and about 45 minutes.
There's no single right answer. The interviewer wants to see you:
- ask good questions instead of jumping in
- sketch a sensible high-level design with boxes and arrows
- reason about **trade-offs** ("a cache makes reads fast, but the data can be stale")
- go deeper on one or two parts when asked

For new-grad and junior roles the bar is fundamentals and clear communication, not memorized architectures.

## A 4-step answer framework

1. **Requirements (~5 min)**
   - *Functional:* what does it do? ("users can shorten a URL; visiting the short URL redirects")
   - *Non-functional:* scale, speed, availability ("100M URLs, redirects in <100ms, must not go down")
2. **Estimates + API (~5 min)**
   - Rough numbers: requests per second, storage per year. Round aggressively.
   - Endpoints: `POST /urls {long_url} -> {short_code}`, `GET /{short_code} -> 302 redirect`
3. **High-level design (~15 min)**
   - Client → load balancer → app servers → database, plus a cache, queue, or CDN where they help.
   - Walk one request through the diagram from start to finish.
4. **Deep dive + trade-offs (~15 min)**
   - Bottlenecks, scaling (replicas, sharding), failure cases, and what you'd do differently at 10x scale.

## Vocabulary to learn first (in this order)

| Concept | One-line meaning |
|---------|------------------|
| Client / server, HTTP, REST API | how a browser or app talks to your backend |
| Database: SQL vs NoSQL | tables with relations vs flexible key-value/document stores |
| Cache (e.g. Redis) | keeps hot data in memory so reads skip the database |
| Load balancer | spreads requests across many servers |
| Horizontal vs vertical scaling | add more machines vs make one machine bigger |
| Replication / sharding | copy data for reliability / split data across machines for size |
| CDN | serves static files (images, video) from servers near the user |
| Message queue (e.g. Kafka, SQS) | lets slow work happen in the background |
| CAP / consistency vs availability | during a network split, choose correct-but-maybe-down or up-but-maybe-stale |

## Study path (weekends, ~1 hr each)

- [ ] Weeks 1–3: [NeetCode System Design for Beginners](https://neetcode.io/courses/system-design-for-beginners). Write a short note per lesson in `notes/`
- [ ] Weeks 4–5: [System Design Primer](https://github.com/donnemartin/system-design-primer): the "Index of system design topics" section
- [ ] Week 6+: one practice design per weekend in `practice/`, using the framework above:
  - [ ] URL shortener
  - [ ] Rate limiter
  - [ ] Chat app
  - [ ] News feed
- [ ] Later: Alex Xu, *System Design Interview Vol. 1*, and [Hello Interview](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction)

Practice talking: explain each design out loud for 10 minutes as if to an interviewer. That's the skill being tested.
