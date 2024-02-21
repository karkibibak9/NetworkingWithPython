# Networking With Scapy 👋

### Project Description
Welcome to Networking With Scapy, a Python project focused on studying and implementing various networking layers using Scapy. This project aims to provide a hands-on learning experience in networking protocols and packet manipulation techniques.

### ✨ Motive
The primary goal of this project is to deepen understanding and practical skills in networking by exploring different layers of the OSI model and implementing them using Scapy. By leveraging Scapy's capabilities, we can craft, send, receive, and analyze packets at different network layers, enabling us to grasp fundamental concepts more effectively.


## Day 1 
#IEEE 802.3
Ethernet is a set of technologies and protocols that are used primarily in LANs. It was first standardized in 1980s by IEEE 802.3 standard. IEEE 802.3 defines the physical layer and the medium access control (MAC) sub-layer of the data link layer for wired Ethernet networks.
Ethernet is classified into two categories: classic Ethernet and switched Ethernet.

## Install

```sh
<%= installCommand %>
```
<% } -%>
<% if (usage) { -%>

## Usage

```sh
<%= usage %>
```
<% } -%>
<% if (testCommand) { -%>

## Run tests

```sh
<%= testCommand %>
```
<% } -%>
<% if (authorName || authorTwitterUsername || authorGithubUsername) { -%>

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](<%= issuesUrl %>). <%= contributingUrl ? `You can also take a look at the [contributing guide](${contributingUrl}).` : '' %>
<% } -%>

## Show your support

Give a ⭐️ if this project helped you!
<% if (authorPatreonUsername) { -%>

[![support us](https://img.shields.io/badge/become-a patreon%20us-orange.svg?cacheSeconds=2592000)](https://www.patreon.com/<%= authorPatreonUsername %>)
<% } -%>

<% if (licenseName && licenseUrl) { -%>

## 📝 License

<% if (authorName && authorGithubUsername) { -%>
Copyright © <%= currentYear %> [<%= authorName %>](https://github.com/<%= authorGithubUsername %>).

<% } -%>
This project is [<%= licenseName %>](<%= licenseUrl %>) licensed.
<% } -%>

***
<%- include('footer.md'); -%>
