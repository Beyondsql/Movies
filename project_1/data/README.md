### Data

Two related datasets carry information about movies, scraped from the websites http://www.boxofficemojo.com and http://www.metacritic.com. 

You can use both of these datasets for project 1 if you like, but there is no simple way to join them provided (DATA CHALLENGE). 


### Fields

**boxofficemojo**: 

* alt_title  (string) - Title and (year) 

* director  (string) - Director 

* domestic_gross (float) - Total theater take in US

* mojo_slug (string) - data was scraped from `www.boxofficemojo.com/movies/?id=` `mojoslug` `.htm`

* opening_per_theater (float) - opening weekend take div by # theaters opening weekend

* opening_weekend_take (float) - gross ticket sales on opening weekend

* production_budget (float) - where available.

* release_date_limited (date) - where available, limited release date

* release_date_wide (date) - wide (or only) release date

* title (string) 

* widest_release (int) - greatest number of theaters simultaneously showing the film

* worldwide_gross (float) - where available, gross of all countries including US

* year (date) - date that the movie was released


**metacritic**: 

* complete (boolean) - were all fields parsed and believed correct?

* director (string) - Director

* genre (list) - can have 0..many. boxofficemojo also lists genres but those are trippin.

* metacritic_page (string) - append to http://www.metacritic.com to get the page this data came from

* metascore (int) - the score derived from critic and user reviews on scale [0..100]

* num_critic_reviews (list) -- number of reviews categorized as [positive, neutral, negative, total]

* num_user_ratings (int) -- number of user ratings (this is different than a review)

* num_user_reviews (list) -- number of reviews categorized as [positive, neutral, negative, total]

* rating (string) -- MPAA rating

* release_date (string) -- YYYY-MM-DD

* runtime_minutes (int) - how long is the movie

* studio (string) - production studio that made the movie

* title (string) - THE TIILE FIGFIEFH:ISEJ

* user_score (decimal) - some kind of weighted average of the user ratings

* year (int) - funny enough, this field is the number of times I recorded the year for each movie
