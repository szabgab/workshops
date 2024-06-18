# Web development in Rust using Rocket

## Announcement

In this workshop we will create a web site using the [Rocket web framework](https://rocket.rs/).
We don't assume any background in web development. We'll use minimal HTML, we'll try to focus on getting started with the Rocket framework

The workshop includes presentations and hands-on work.

The workshop will be via Zoom (link will be announced close to the event)
Language: English.
Workshop lead: [Gabor Szabo](https://szabgab.com/)
Requirements: Basic familiarity with writing Rust will be enough.
Length: up to 2 hours.

Cost: This workshop is free of charge thanks to the people who support me via one of the following systems: [Github sponsor](https://github.com/sponsors/szabgab/), [Patreon](https://www.patreon.com/szabgab), or directly via [PayPal](https://www.paypal.com/paypalme/szabgab).



## Why Rocket?

* [Rocket](https://rocket.rs/)

## Articles about Rocket

* [Rocket - web development with Rust](https://rust.code-maven.com/rocket)


## Rocket skeleton

There is
* [Cargo generate](https://github.com/cargo-generate/)
* [Cargo generate](https://github.com/topics/cargo-generate)

But I did not know about it so I created

* [Rocket Starter](https://crates.io/crates/rocket-starter)


```
cargo install rocket-starter
```

```
cargo install cargo-watch
cargo watch -x run
```

* [rocket_dyn_templates](https://crates.io/crates/rocket_dyn_templates)
* [tera](https://crates.io/crates/tera)


* [Rocket Discussion forum](https://github.com/rwf2/Rocket/discussions)

In this meeting we covered
* GET and a tiny bit POST requests.
* Request routing.
* Templates - Tera
* 404 catcher.
* A little bit getting parameters via GET and POST requests.
* Testing the simple examples.
* We used the rocket-starter with the following flags:  `--simple`, `--tera1`, `--tera2` `--tera-module`.
* We mentioned that it is using Tokio and that we can use `async`, but we have not tried it.


