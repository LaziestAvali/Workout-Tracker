# Workout API
That project started as part of studying "Backend Developer" from
[roadmap](https://roadmap.sh/projects/fitness-workout-tracker).
For that project I am using Python with FastAPI as framework.
# Project start
nothing here... for now
# Project usage
nothing here... for now
# Roadmap | Plan of project
## Basic plan
While this project is in development, I will try to note progress in this plan.
- [ ] Design Project;
  - [ ] Project structure;
  - [ ] DB structure;
  - [ ] API structure;
- [ ] Create main parts project;
  - [ ] Create DB
    - [ ] Create all tables
    - [ ] Add test data
    - [ ] Create start script to deploying to another machines [^1]
  - [ ] Create API
    - [ ] Basic AUTH
    - [ ] Creating Workouts
    - [ ] Updating/Deleting Workouts (mark as deleted or REAL delete?)
    - [ ] Workouts Schedule/Lists
    - [ ] Workout Reports
    - [ ] Exercises adding [^2]
    - [ ] Publish Workouts for other users [^2]
- [ ] Add JWT authentication to app;
  - [ ] Destroy old AUTH and replace it with access token
  - [ ] Update it to OAuth2 with refresh token [^2]
  - [ ] Save Refresh token at db [^2]
- [ ] Create unit-tests (at least 10);
- [ ] Add Documentation (OpenAPI specs) via build-ins in FastAPI;

[^1]: Does NOT include as a "required" on roadmap, but it will be implemented to testing on another PCs. <br/>
[^2]: A logical extension of the project that is NOT used in the original

## Advanced plan
Starts only if I'll be able to continue that project. It has only advanced parts, that doesn't implemented in
[roadmap](https://roadmap.sh/projects/fitness-workout-tracker), but in Backend Roadmap.
If that project get enough upvotes at roadmap, then I'll be start that 100%
- [ ] Add Server Side caching with Redis (?)
- [ ] Rebuild DB as ORM
- [ ] Implement HTTP**S**
- [ ] Containerize app
- [ ] Add CI
  - [ ] Auto building after commiting changes
  - [ ] Autotests
- [ ] Rewrite project as microservices
  - [ ] Auth service
  - [ ] Workout service
- Add Message Broker (ApacheKafka) [^3]
- Add Search Engine (Elasticsearch) [^3]

[^3]: Only if it will be available. At start of the project I am not fully understand how much features I can add. 