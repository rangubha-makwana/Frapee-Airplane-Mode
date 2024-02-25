SELECT
    A.name,
    COALESCE(SUM(T.total_amount), 0) AS revenue
FROM
    `tabAirline` A
JOIN
    `tabAirplane` AP ON A.name = AP.airline
JOIN
    `tabAirplane Flight` F ON AP.name = F.airplane
JOIN
    `tabAirplane Ticket` T ON F.name = T.flight
GROUP BY
    A.name;


SELECT
    A.airline_id,
    A.airline_name,
    COALESCE(SUM(T.total_amount), 0) AS revenue
FROM
    Airline A
LEFT JOIN
    Airplane AP ON A.airline_id = AP.airline_id
LEFT JOIN
    Flight F ON AP.airplane_id = F.airplane_id
LEFT JOIN
    Ticket T ON F.flight_id = T.flight_id
GROUP BY
    A.airline_id, A.airline_name;

