/*
    I'm not too sure what "registration" means in this context. Assuming it's a milestone
    event we would like to encourage more conversion on, keeping track of this flag can:
        - produce a conversion rate
        - divide the patients into two cohort (registered vs not-registered)
    The conversion rate can be used at a strategic level to:
        - track overall progress on the journey
        - identify opportunities to target certain group of the population for campaigning
        - monitor the effectiveness of any campaign investment
        - etc.
    The cohort flag can be used as:
        - a segmenting criteria to analyse product usage pattern
        - a slicer to monitor key metrics such as appointment cancellation rate
        - a feature in training predicative models
        - etc.
*/
SELECT
    COUNT(CASE WHEN registration_date IS NOT NULL THEN 1 END) AS registered_patients
    , COUNT(*) AS total_patients
FROM
    patients
;