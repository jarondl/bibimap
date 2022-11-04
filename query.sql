select yishuv_stat2011 as YISHUV_STA,
       sum(iif(PARTY_NAME in ('מחל','ט','שס','ג','ב'), 1.0*result,0.0)) / sum(1.0* result) as bibi
from regions join
results using (SEMEL_YISHUV, KALPI2022) join
parties using (PARTY_ID) group by yishuv_stat2011;
