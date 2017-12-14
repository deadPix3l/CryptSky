# CryptSky

CryptSky is an open source, fully python ransomware PoC. It's main purpose is
not to be run like most software projects, but to be read for educational
purposes.

Aside from very minor testing to ensure there are no syntax errors, no testing
has been done. This may occur at a later time to ensure it performs in all
expected environments,but that is not the point. The point is to be a simple
to read PoC that makes for an easy example of what ransomware is and how it
works. And hopefully, this can lead to a better understanding of ransomware in 
the network defense and sysadmin communities.

**Warning: This project is young and incomplete. It will encrypt and decrypt
files. That's about it. No key generation, no sending the key back over a
secure channel, no dropping new files or wallpapers or whatever. I'll get to
that. Maybe. Open an issue if you so desire, pull requests welcome.**

## Why?

There is a severe lack of open source ransomware, and for good reason! But by
having so few examples, and those examples being inaccurate (intentionally bad
code with flaws), or just too complicated, it doesn't leave much to analyze
and learn from. People seem to think that ransomware is hard to write. That
it's this complex, hard to develop, hard to RE, and hard to prevent beast. A
quick read through of this codebase will prove that's not true. Im hoping this
can lead to better signatures, a better understanding of how ransomware works
and what can be done to stop it, and an overall safer internet.

## Objections!

But aren't you worried someone will abuse it for profit?

- Not really. There are plenty of much better, more advanced ransomware out there.
 Even if they do, it's hopefully few compared to the good it will do.

But when they do, it would be your fault!

- Nope! I only wrote it. I didnt deploy it, I didnt sell it, it's not my
problem. Hopefully nobody uses it for evil but thats the price to be paid for
good. There's always someone who will do it.

But...

- Alright. Bottom line. Security is a very reactive business. To make the
world more secure you first have to make it less secure. To make better AV and
signatures, you must first make better malware. And that's what we're doing
here.
