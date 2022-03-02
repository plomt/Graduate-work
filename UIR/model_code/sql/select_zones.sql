SELECT zone1_x, zone1_y, zone1_d, zone2_x, zone2_y, zone2_d, zone3_x, zone3_y, zone3_d, zone4_x, zone4_y, zone4_d
FROM public.webapp_zones
WHERE id = (SELECT MAX(id)
            FROM public.webapp_zones);