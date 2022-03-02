SELECT fuel, termfuel, clad, tube
FROM public.webapp_temperature
WHERE id = (SELECT MAX(id)
            FROM public.webapp_temperature);