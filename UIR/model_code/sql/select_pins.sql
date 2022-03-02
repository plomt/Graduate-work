SELECT pin1_void1, pin1_fuel, pin1_void2, pin1_clad, pin2_termfuel, pin2_clad
FROM public.webapp_pins
WHERE id = (SELECT MAX(id)
            FROM public.webapp_pins);