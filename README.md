# smpl Recipe

Data collection and management API for smpl Recipe app built with Python, Django, and Postres.


## Overview

Recipe web application developed as a minimum viable product showcasing a minimalistic, user-friendly, approach to consuming recipes.

This app exists in three parts:

* Client-facing frontend - https://github.com/mattvox/smpl-recipe-client
* Client-serving API - https://github.com/mattvox/smpl-recipe-api
* Data management and retrieval API - (You are here!)

### Why decouple?

_NOTE: This section has been duplicated on every readme pertaining to this app. Scroll down to the Technical section for service-specific information._

This project first began solely in Python and Django, handling everything from data collection and management, data retrieval, and serving it all up client-side. As the only developer on the project, questions and concerns about speed of development and deployment continued to come up. Not being an expert with managing deployments and servers certainly influenced this decision.

The first service to be decoupled from the main application was the data collection and management layer. For this MVP, a web scraper written in Python was used to collect and store formatted recipe data into a Postgres database. Since the scraper was written in Python, it only made sense to use Django for its wonderful, out-of-the-box admin setup, which made managing the collected data extremely simple. Deploying this service was trivial since I had already configured Gunicorn and Nginx on the Linode VPS used for this app.

With the data collection and management separated from the main app, a small Node/Express server was created serve the frontend and query the database for recipe data. During development, data requests were proxied to the Node server, but in production the client-side was simply bundled up and served up without the need for a proxy.

While these changes certainly sped up development and deployment, I didn't like having to redeploy the Node server each time a change was made to the frontend. Since both servers rarely changed in relation to how often the client was updated, a decision was made to further separate the client and APIs to further increase development speed, testing and ease of deployment and open up other hosting possibilities.


## Technical

* Data collection and management API powered by Python and Django.
* Postgres chosen as the database for its performance, compatibility, and ease of use with multiple stacks.
* Python library, Psycopg2 is used to connect database.
* Beautiful Soup used to scrape test data from various sites which use the h.recipe microformat.
* Django's built in admin used to get up and running extremely fast, removing initial data management as a concern within the scope of this project.
* Django's management commands easily handle running the scraper from the command line and can be effortlessly integrated with Celery to automate the process in the future.

To see more documentation for another part of the app, please visit the links above in the Overview section.


## Deployment

This app is currently hosted on a Linode VPS with both Gunicorn and Nginx acting as a proxy, fully managed and setup by me.


## Development Roadmap

This app is still in development; future enhancements are expected to include:

*needs more documentation*
