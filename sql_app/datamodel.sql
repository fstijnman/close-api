CREATE TABLE "Venues" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "addressLine1" varchar,
  "addressLine2" varchar,
  "city" varchar,
  "postalCode" varchar,
  "email" varchar,
  "phone" varchar,
  "priceId" int,
  "createdOn" timestamp
);

CREATE TABLE "Events" (
  "id" SERIAL PRIMARY KEY,
  "venueId" int,
  "name" varchar,
  "startDate" datetime,
  "endDate" datetime,
  "priceId" varchar,
  "createdOn" timestamp
);

CREATE TABLE "CategoryEvent" (
  "id" SERIAL PRIMARY KEY,
  "eventId" int,
  "name" varchar
);

CREATE TABLE "CategoryVenue" (
  "id" SERIAL PRIMARY KEY,
  "venueId" int,
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
  "priceRegular" int,
  "priceStudent" int,
  "priceAbove60" int,
  "priceUnder18" int,
  "priceCJP" int,
  "priceMuseumCard" int
);

CREATE TABLE "OpeningHoursVenue" (
  "id" SERIAL PRIMARY KEY,
  "venueId" int,
  "fromDate" datetime,
  "toDate" datetime,
  "weekday" varchar,
  "startHour" datetime,
  "endHour" datetime
);

CREATE TABLE "OpeningHoursEvent" (
  "id" SERIAL PRIMARY KEY,
  "eventId" int,
  "fromDate" datetime,
  "toDate" datetime,
  "weekday" varchar,
  "startHour" datetime,
  "endHour" datetime
);

ALTER TABLE "Venues" ADD FOREIGN KEY ("id") REFERENCES "Events" ("venueId");

ALTER TABLE "EventPrice" ADD FOREIGN KEY ("id") REFERENCES "Events" ("priceId");

ALTER TABLE "OpeningHoursVenue" ADD FOREIGN KEY ("venueId") REFERENCES "Venues" ("id");

ALTER TABLE "OpeningHoursEvent" ADD FOREIGN KEY ("eventId") REFERENCES "Events" ("id");

ALTER TABLE "CategoryVenue" ADD FOREIGN KEY ("venueId") REFERENCES "Venues" ("id");

ALTER TABLE "CategoryEvent" ADD FOREIGN KEY ("eventId") REFERENCES "Events" ("id");

ALTER TABLE "Venues" ADD FOREIGN KEY ("priceId") REFERENCES "VenuePrice" ("id");
