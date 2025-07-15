Feature: Model endpoint check

    Scenario Outline: AT-05 Check model endpoint calls (GET) all
        When  user call model GET endpoint as /api/<path>
        Then  response should match model list validations

    Examples:
      | path               |
      | achievements       |
      | gardens            |
      | items              |
      | levels             |
      | minigames          |
      | plants             |
      | puzzles            |
      | survivals          |
      | zombies            |

    Scenario Outline: AT-06 Check model endpoint calls (GET) all with args
        When  user call model GET endpoint as /api/<path>
        Then  response should match model list validations

    Examples:
      | path                              |
      | achievements?name=Better+Off+Dead |
      | gardens?name=Night+Garden         |
      | items?name=Waterin+can            |
      | levels?level=4-7                  |
      | minigames?name=Seeing+Stars       |
      | plants?name=Spikeweed             |
      | puzzles?name=I,+Zombie            |
      | survivals?name=Survival:+Pool     |
      | zombies?name=Zombie+Yeti          |

    Scenario Outline: AT-07 Check model endpoint calls (GET) all no matches
        When  user call model GET endpoint as /api/<path>
        Then  user get error from api with code 404

    Examples:
      | path                         |
      | achievements?name=not-exists |
      | gardens?name=not-exists      |
      | items?name=not-exists        |
      | levels?level=not-exists      |
      | minigames?name=not-exists    | 
      | plants?name=not-exists       |
      | puzzles?name=not-exists      |
      | survivals?name=not-exists    |
      | zombies?name=not-exists      |

    Scenario Outline: AT-08 Check model endpoint calls (GET) all with bad args
        When  user call model GET endpoint as /api/<path>
        Then  user get error from api with code 404

    Examples:
      | path                                 |
      | achievements?non_existing_field=true |
      | gardens?non_existing_field=true      |
      | items?non_existing_field=true        |
      | levels?non_existing_field=true       |
      | minigames?non_existing_field=true    |
      | plants?non_existing_field=true       |
      | puzzles?non_existing_field=true      |
      | survivals?non_existing_field=true    |
      | zombies?non_existing_field=true      |

    Scenario Outline: AT-09 Check model endpoint calls (GET) by id
        When  user call model GET by Id endpoint as /api/<path>/<model_id>
        Then  response should match model element validations

    Examples:
      | path         | model_id                             |
      | achievements | ef71c066-30db-45b1-bdc3-6038b74be722 |
      | gardens      | 160325cf-a53b-4493-9b09-c816818f0f7b |
      | items        | 43264728-44b7-466c-83b5-751181615549 |
      | levels       | 6e20d17b-8def-48fd-93f4-f7e546aeb3cd |
      | minigames    | 2fc814f2-3da5-47e9-b555-298dd8e7a4d8 |
      | plants       | 012b225e-323a-4c73-b011-67de27a03fdb |
      | puzzles      | 65737522-4128-4ab8-aa58-baa159e947ae |
      | survivals    | 6ab34871-79f2-44a9-b31e-d912f648ab4c |
      | zombies      | f95cec84-f634-4d08-968d-ae0061fcfe7d |

    Scenario Outline: AT-10 Check model endpoint calls (GET) by id - not found
        When  user call model GET by Id endpoint as /api/<path>/<model_id>
        Then  user get error from api with code 404

    Examples:
      | path         | model_id                             |
      | achievements | ef71c066-30db-45b1-bdc3-6038b74be7ff |
      | gardens      | 160325cf-a53b-4493-9b09-c816818f0fff |
      | items        | 43264728-44b7-466c-83b5-7511816155ff |
      | levels       | 6e20d17b-8def-48fd-93f4-f7e546aeb3ff |
      | minigames    | 2fc814f2-3da5-47e9-b555-298dd8e7a4ff |
      | plants       | 012b225e-323a-4c73-b011-67de27a03fff |
      | puzzles      | 65737522-4128-4ab8-aa58-baa159e947ff |
      | survivals    | 6ab34871-79f2-44a9-b31e-d912f648abff |
      | zombies      | f95cec84-f634-4d08-968d-ae0061fcfeff |

    Scenario Outline: AT-11 Check model endpoint calls (POST) missing req data
        Given load request data from features/data/AT-11/<request>
        When  user call model POST endpoint as /api/<path>
        Then  user get error from api with code 422
        And   request data is cleared out

    Examples:
      | request          | path         |
      | achievement.json | achievements |
      | garden.json      | gardens      |
      | item.json        | items        |
      | level.json       | levels       |
      | minigame.json    | minigames    |
      | plant.json       | plants       |
      | puzzle.json      | puzzles      |
      | survival.json    | survivals    |
      | zombie.json      | zombies      |
    
    Scenario Outline: AT-12 Check model endpoint calls (PATCH) by id - no payload
        When  user call model PATCH endpoint as /api/<path>/<model_id>
        Then  user get error from api with code 422

    Examples:
      | path         | model_id                             |
      | achievements | ef71c066-30db-45b1-bdc3-6038b74be7ff |
      | gardens      | 160325cf-a53b-4493-9b09-c816818f0fff |
      | items        | 43264728-44b7-466c-83b5-7511816155ff |
      | levels       | 6e20d17b-8def-48fd-93f4-f7e546aeb3ff |
      | minigames    | 2fc814f2-3da5-47e9-b555-298dd8e7a4ff |
      | plants       | 012b225e-323a-4c73-b011-67de27a03fff |
      | puzzles      | 65737522-4128-4ab8-aa58-baa159e947ff |
      | survivals    | 6ab34871-79f2-44a9-b31e-d912f648abff |
      | zombies      | f95cec84-f634-4d08-968d-ae0061fcfeff |

    Scenario Outline: AT-13 Check model endpoint calls (PATCH) by id - not found
        Given load request data from features/data/AT-13/<request>
        When  user call model PATCH endpoint as /api/<path>/<model_id>
        Then  user get error from api with code 404

    Examples:
      | path         | model_id                             | request          |
      | achievements | ef71c066-30db-45b1-bdc3-6038b74be7ff | achievement.json |
      | gardens      | 160325cf-a53b-4493-9b09-c816818f0fff | garden.json      |
      | items        | 43264728-44b7-466c-83b5-7511816155ff | item.json        |
      | levels       | 6e20d17b-8def-48fd-93f4-f7e546aeb3ff | level.json       |
      | minigames    | 2fc814f2-3da5-47e9-b555-298dd8e7a4ff | minigame.json    |
      | plants       | 012b225e-323a-4c73-b011-67de27a03fff | plant.json       |
      | puzzles      | 65737522-4128-4ab8-aa58-baa159e947ff | puzzle.json      |
      | survivals    | 6ab34871-79f2-44a9-b31e-d912f648abff | survival.json    |
      | zombies      | f95cec84-f634-4d08-968d-ae0061fcfeff | zombie.json      |

    Scenario Outline: AT-14 Check model endpoint calls (PATCH) by id - not updatable
        Given load request data from features/data/AT-14/<request>
        When  user call model PATCH endpoint as /api/<path>/<model_id>
        Then  user get error from api with code <code>

    Examples:
      | path         | model_id                              | request              | code |
      | achievements | ef71c066-30db-45b1-bdc3-6038b74be722  | request-created.json | 304  |
      | gardens      | 160325cf-a53b-4493-9b09-c816818f0f7b  | request-created.json | 304  |
      | items        | 43264728-44b7-466c-83b5-751181615549  | request-created.json | 304  |
      | levels       | 6e20d17b-8def-48fd-93f4-f7e546aeb3cd  | request-created.json | 304  |
      | minigames    | 2fc814f2-3da5-47e9-b555-298dd8e7a4d8  | request-created.json | 422  |
      | plants       | 012b225e-323a-4c73-b011-67de27a03fdb  | request-created.json | 304  |
      | puzzles      | 65737522-4128-4ab8-aa58-baa159e947ae  | request-created.json | 304  |
      | survivals    | 6ab34871-79f2-44a9-b31e-d912f648ab4c  | request-created.json | 304  |
      | zombies      | f95cec84-f634-4d08-968d-ae0061fcfe7d  | request-created.json | 304  |
      | achievements | ef71c066-30db-45b1-bdc3-6038b74be722  | request-updated.json | 304  |
      | gardens      | 160325cf-a53b-4493-9b09-c816818f0f7b  | request-updated.json | 304  |
      | items        | 43264728-44b7-466c-83b5-751181615549  | request-updated.json | 304  |
      | levels       | 6e20d17b-8def-48fd-93f4-f7e546aeb3cd  | request-updated.json | 304  |
      | minigames    | 2fc814f2-3da5-47e9-b555-298dd8e7a4d8  | request-updated.json | 422  |
      | plants       | 012b225e-323a-4c73-b011-67de27a03fdb  | request-updated.json | 304  |
      | puzzles      | 65737522-4128-4ab8-aa58-baa159e947ae  | request-updated.json | 304  |
      | survivals    | 6ab34871-79f2-44a9-b31e-d912f648ab4c  | request-updated.json | 304  |
      | zombies      | f95cec84-f634-4d08-968d-ae0061fcfe7d  | request-updated.json | 304  |

    Scenario Outline: AT-15 Check model endpoint calls (PATCH) by id - invalid field
        Given load request data from features/data/AT-15/request.json
        When  user call model PATCH endpoint as /api/<path>/<model_id>
        Then  user get error from api with code <code>

    Examples:
      | path         | model_id                             | code |
      | achievements | ef71c066-30db-45b1-bdc3-6038b74be722 | 304  |
      | gardens      | 160325cf-a53b-4493-9b09-c816818f0f7b | 304  |
      | items        | 43264728-44b7-466c-83b5-751181615549 | 304  |
      | levels       | 6e20d17b-8def-48fd-93f4-f7e546aeb3cd | 304  |
      | minigames    | 2fc814f2-3da5-47e9-b555-298dd8e7a4d8 | 422  |
      | plants       | 012b225e-323a-4c73-b011-67de27a03fdb | 304  |
      | puzzles      | 65737522-4128-4ab8-aa58-baa159e947ae | 304  |
      | survivals    | 6ab34871-79f2-44a9-b31e-d912f648ab4c | 304  |
      | zombies      | f95cec84-f634-4d08-968d-ae0061fcfe7d | 304  |

    Scenario Outline: AT-16 Check model endpoint calls (DELETE) by id - not found
        When  user call model DELETE endpoint as /api/<path>/<model_id>
        Then  user get error from api with code 404

    Examples:
      | path         | model_id                             |
      | achievements | ef71c066-30db-45b1-bdc3-6038b74be7ff |
      | gardens      | 160325cf-a53b-4493-9b09-c816818f0fff |
      | items        | 43264728-44b7-466c-83b5-7511816155ff |
      | levels       | 6e20d17b-8def-48fd-93f4-f7e546aeb3ff |
      | minigames    | 2fc814f2-3da5-47e9-b555-298dd8e7a4ff |
      | plants       | 012b225e-323a-4c73-b011-67de27a03fff |
      | puzzles      | 65737522-4128-4ab8-aa58-baa159e947ff |
      | survivals    | 6ab34871-79f2-44a9-b31e-d912f648abff |
      | zombies      | f95cec84-f634-4d08-968d-ae0061fcfeff |