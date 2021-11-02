CREATE TABLE "Venues" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "addressLine1" varchar,
  "addressLine2" varchar,
  "city" varchar,
  "postalCode" varchar,
  "email" varchar,
  "phone" varchar,
  "createdOn" timestamp
);

CREATE TABLE "Events" (
  "id" SERIAL PRIMARY KEY,
  "venueId" int,
  "name" varchar,
  "categoryId" int,
  "startDate" datetime,
  "endDate" datetime,
  "priceId" varchar,
  "createdOn" timestamp
);

CREATE TABLE "Category" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "EventPrice" (
  "id" SERIAL PRIMARY KEY,
  "priceRegular" int,
  "priceStudent" int,
  "priceAbove60" int,
  "priceUnder18" int,
  "priceCJP" int,
  "priceMuseumCard" int
);

CREATE TABLE "VenuePrice" (
  "id" SERIAL PRIMARY KEY,
  "venueId" int,
  "priceRegular" int,
  "priceStudent" int,
  "priceAbove60" int,
  "priceUnder18" int,
  "priceCJP" int,
  "priceMuseumCard" int
);

CREATE TABLE "OpeningHours" (
  "id" SERIAL PRIMARY KEY,
  "venueId" int,
  "fromDate" datetime,
  "toDate" datetime,
  "weekday" varchar,
  "startHour" datetime,
  "endHour" datetime
);

ALTER TABLE "Venues" ADD FOREIGN KEY ("id") REFERENCES "Events" ("venueId");

ALTER TABLE "EventPrice" ADD FOREIGN KEY ("id") REFERENCES "Events" ("priceId");

ALTER TABLE "VenuePrice" ADD FOREIGN KEY ("venueId") REFERENCES "Venues" ("id");

ALTER TABLE "Category" ADD FOREIGN KEY ("id") REFERENCES "Events" ("categoryId");

ALTER TABLE "OpeningHours" ADD FOREIGN KEY ("venueId") REFERENCES "Venues" ("id");
