CREATE TABLE parties(
    party_id integer not null,
    party_name text not null);
CREATE TABLE results(
    SEMEL_YISHUV integer not null,
    KALPI2022 integer not null,
    KALPI_FULL text not null,
    PARTY_ID integer not null,
    result integer not null);
CREATE TABLE regions(
    SEMEL_YISHUV text not null,
    SHEM_YISHUV text not null,
    KALPI2022 integer not null,
    Stat2011 integer not null,
    yishuv_stat2011 integer not null
);

.mode csv
.import --skip 1 expb_parties.csv parties
.import --skip 1 expb_results.csv results
.import --skip 1 ../regions.csv regions
