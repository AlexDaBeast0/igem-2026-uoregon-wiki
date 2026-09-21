---
layout: page
permalink: /software

title: Wiki Search
subtitle: This is the wiki search page.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---


# Introduction

Every iGEM team begins by asking whether anyone has tackled their problem before. The iGEM Wiki Search Engine is a tool built to make information from past iGEM projects more accessible. Each year, hundreds of teams document their research, experimental methods, project designs and results on their wiki page, yet finding specific information across these wikis is challenging, as they are hosted as separate websites. General search engines cover them poorly and inconsistently, so the only way to find a relevant project is to already know the team’s name and year. 

Our search engine effectively addresses this problem by collecting and indexing information from iGEM team wikis, allowing users to search across multiple teams and years through a single interface. Instead of manually navigating individual websites, users can enter keywords and discover relevant projects and research findings from past teams. Ultimately, this tool encourages knowledge sharing between teams and helps future teams build upon existing work. 

# Prior work and how we improve on it

# Key Features Overview

## 1. Centralized Wiki Search

Instead of manually navigating individual team wikis, users can search across multiple teams and competition years from a single platform. 

- **Cross-team search:** Search through the content of multiple iGEM team wikis simultaneously, making it easier to discover projects related to a specific research topic
- **Full text search:** Search the actual content of wiki pages rather than relying solely on project titles, team names, or predefined categories
- **Multiple Years:** Explore iGEM projects dating back to 2022, allowing users to discover previous research and investigate how different teams have approached similar challenges
- **Keyword-based:** Enter specific terms, techniques, genetic components, or research topics to identify relevant wiki pages
- **Direct Access to Original Sources:** Open relevant pages directly to their original team wikis to explore the entire project documentation

## 2. Automated Wiki Collection and Processing

Our web crawler systematically collects and processes information from iGEM team wikis, creating a centralized database of previous projects.

- **Automated Web Crawling:** The crawler visits individual team wikis and follows internal links to discover additional pages containing project documentation
- **HTML Content Extraction:** Requests, BeautifulSoup, and Trafilatura retrieve and extract relevant text from wiki pages while removing unnecessary HTML elements
- **JavaScript Rendering Support:** Playwright adds a rendering step for wikis that load content using JavaScript
- **Repeatition Prevention:** Previously discovered URLs are tracked to prevent the crawler from  processing the same pages
- **Controlled Crawling:** Configurable limits on crawling depth, pages per team, and request frequency help manage resource usage and avoid unnecessary requests

## 3. Full-Text Indexing and Search

Our search engine uses SQLite and its Full-Text Search 5 (FTS5) extension to organize collected wiki content and retrieve relevant information.

- **Centralized Database:** Extracted wiki content is stored alongside team names, competition years, page titles, and original URLs
- **Full-Text Indexing:** SQLite FTS5 creates a searchable index of wiki content, allowing the system to locate pages containing specific keywords and research terms
- **Efficient Information Retrieval:** Search queries are processed against the indexed database

## 4. Extensible Architecture

# How It Works

Our search engine consists of four main components: a web crawler, a database, a search backend, and a user interface. 

*make a flowchart to put here (igem team wikis → python web crawler → sqlite database + fts5 index → fastapi backend → search interface)* 

## Step 1: Collecting wiki content

We developed a Python web crawler that systematically visits iGEM team wikis and extracts their text content.

The crawler uses libraries such as Requests, BeautifulSoup, and Trafilatura to retrieve and process HTML pages. For websites that rely on JavaScript to display their content, Playwright provides an additional rendering step.

This allows the crawler to collect information from different wiki structures while avoiding unnecessary downloads of media files.

## Step 2: Building the searchable database

The extracted wiki content is stored in an SQLite database, along with relevant information such as the team name, year, page title, and original URL.

We use SQLite's Full-Text Search 5 (FTS5) extension to create a searchable index of the collected text. This allows the system to identify pages containing relevant terms without having to scan every stored document for each query.

## Step 3: Processing search queries

When a user enters a search query, the frontend sends it to a FastAPI backend, which then searches the indexed database for matching wiki pages and returns the relevant results to the frontend.

Because the search takes place on the server, users do not need to download the entire database or run the crawler themselves.

## Step 4: Displaying results

The frontend displays matching wiki pages and provides links to their sources. Users can then navigate directly to the relevant sections of past projects to explore experimental methods, results, designs, and other documentation.

In this way, the search engine serves as a discovery tool rather than a replacement for the original team wikis.

## Step 5. How to Access It

TBD
