drop table if exists calendar;

create table calendar (
date_actual date not null,
day_name    varchar(9) not null,
day_of_week int not null,
is_weekend boolean not null,
is_holiday boolean not null,
primary key (date_actual)
);

create index calendar_pk__idx on calendar(date_actual);

insert into calendar
with holidays as 
(
select '1-1' as hday union all
select '6-1' union all
select '8-3' union all
select '15-4' union all
select '17-4' union all
select '18-4' union all
select '1-5' union all
select '26-5' union all
select '05-6' union all
select '6-6' union all
select '10-6' union all
select '16-6' union all
select '15-8' union all
select '20-9' union all
select '3-10' union all
select '31-10' union all
select '1-11' union all
select '25-12' union all
select '26-12')

select date_actual
    , day_name
    , day_of_week 
    , is_weekend
    , case when holidays.hday is not null
        then true
        else false end as is_holiday from (
select 
       date::date as date_actual,
       to_char(date, 'tmday') as day_name,
       extract(isodow from date) as day_of_week,
       case
           when extract(isodow from date) in (6, 7) then true
           else false
           end as is_weekend
from generate_series(date '2022-01-01',
                       date '2023-01-01',
                       interval '1 day') as t(date)
order by 1) t left join holidays
    on holidays.hday = concat(extract(day from t.date_actual)::text,'-',extract(month from t.date_actual)::text);
