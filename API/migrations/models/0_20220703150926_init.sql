-- upgrade --
CREATE TABLE IF NOT EXISTS "githubTable" (
    "repo_name" VARCHAR(256) NOT NULL  PRIMARY KEY,
    "repo_desc" TEXT NOT NULL,
    "date_created" TIMESTAMPTZ NOT NULL,
    "last_push_date" TIMESTAMPTZ NOT NULL,
    "language" VARCHAR(100) NOT NULL,
    "no_of_forks" INT NOT NULL,
    "no_of_stars" INT NOT NULL,
    "no_of_watches" INT NOT NULL,
    "no_of_contributors" INT NOT NULL,
    "no_of_commits" INT NOT NULL,
    "issues" INT NOT NULL,
    "pull_requests" INT NOT NULL,
    "asa_id" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "redditPostTable" (
    "post_id" VARCHAR(255) NOT NULL  PRIMARY KEY,
    "title" TEXT NOT NULL,
    "text" TEXT NOT NULL,
    "score" INT NOT NULL,
    "num_of_comments" INT NOT NULL,
    "time_created" TIMESTAMPTZ NOT NULL,
    "url" TEXT NOT NULL,
    "sentiment_score" DOUBLE PRECISION NOT NULL,
    "asa_id" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "redditCommentTable" (
    "comment_id" VARCHAR(255) NOT NULL  PRIMARY KEY,
    "body" TEXT NOT NULL,
    "score" INT NOT NULL,
    "time_created" TIMESTAMPTZ NOT NULL,
    "sentiment_score" DOUBLE PRECISION NOT NULL,
    "post_id" VARCHAR(255) NOT NULL REFERENCES "redditPostTable" ("post_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "twitterTable" (
    "tweet_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "tweet" TEXT NOT NULL,
    "posted_at" TIMESTAMPTZ NOT NULL,
    "day_of_week" INT NOT NULL,
    "day" INT NOT NULL,
    "month" INT NOT NULL,
    "year" INT NOT NULL,
    "hour" INT NOT NULL,
    "mins" INT NOT NULL,
    "likes" INT NOT NULL,
    "retweets" INT NOT NULL,
    "sentiment_score" DOUBLE PRECISION NOT NULL,
    "asa_id" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
