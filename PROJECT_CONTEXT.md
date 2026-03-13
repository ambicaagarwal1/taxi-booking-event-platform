# TAXI BOOKING EVENT PLATFORM - PROJECT CONTEXT

**Last Updated:** 2024-01-XX
**Current Phase:** Phase 1 - Foundation Solidification
**Next Steps:** Environment Configuration & JWT Authentication

---

## 📌 PROJECT OBJECTIVE

Building a simplified ride booking backend platform (Uber/Ola style) as a **learning platform** to master:
- API design
- Microservices architecture
- Containerization
- Event streaming
- Data pipelines
- Backend data platform engineering

**Key Focus:** Gradual evolution from simple to production-style architecture with deep understanding of each component.

---

## 🏗️ CURRENT ARCHITECTURE

```
Client
   ↓
FastAPI User Service
   ↓
PostgreSQL Database
   ↓
Docker Containers
   ↓
Docker Compose Network
```

---

## ✅ IMPLEMENTED FEATURES

### 1. Dockerized FastAPI Backend
- FastAPI application running in Docker container
- PostgreSQL container with persistent volume
- Docker Compose for orchestration

### 2. User Registration API
**Endpoint:** `POST /users/register`

**Fields:**
- name
- email
- phone
- password

**Validations:**
- Phone must be 10 digits
- Phone must be unique
- Password must be at least 8 characters
- Password must contain one uppercase letter
- Password must contain one special character

**Security:**
- Password hashing before storage
- UUID-based user IDs
- Unique phone number constraint

### 3. Project Structure
```
backend/
   user-service/
       app/
           main.py
           routes/
           schemas/
           database/
           utils/
docker-compose.yml
```

### 4. Version Control
- Git initialized
- Project pushed to GitHub

---

## 🎯 CURRENT TECH STACK

| Component | Technology |
|-----------|-----------|
| Backend Framework | FastAPI (Python) |
| Database | PostgreSQL |
| Containerization | Docker + Docker Compose |
| Version Control | Git + GitHub |
| Development Environment | VS Code with Remote SSH to cloud VM |
| Operating System | Windows (local), Linux (cloud VM) |

---

## 🚀 LONG-TERM ARCHITECTURE VISION

```
Client Applications
      ↓
API Gateway
      ↓
Microservices (FastAPI)
      ↓
Event Streaming Layer (Kafka)
      ↓
Stream Processing (Spark)
      ↓
Data Warehouse (Snowflake)
```

---

## 📋 COMPLETE ROADMAP

### **PHASE 1: Solidify Foundation** ⬅️ **CURRENT PHASE**
**Timeline:** Week 1-2
**Status:** In Progress

**Goals:**
- Make current service production-ready
- Add configuration management
- Implement authentication
- Add logging and monitoring
- Write tests

**Tasks:**
- [ ] Step 1.1: Add Configuration Management (environment variables, pydantic-settings)
- [ ] Step 1.2: Improve API Design (versioning, standardized responses, health checks)
- [ ] Step 1.3: Add Structured Logging (structlog/JSON logging, correlation IDs)
- [ ] Step 1.4: Add Basic Tests (pytest, unit tests, integration tests)

---

### **PHASE 2: Authentication & User Management**
**Timeline:** Week 3-4
**Status:** Not Started

**Goals:**
- Complete user service functionality
- Implement JWT authentication
- Add protected APIs
- Implement RBAC

**Tasks:**
- [ ] Step 2.1: JWT Authentication (login, token generation, middleware, refresh tokens)
- [ ] Step 2.2: Protected User APIs (GET/PUT /users/me, admin endpoints)
- [ ] Step 2.3: Role-Based Access Control (user/driver/admin roles, permission decorators)

---

### **PHASE 3: Add Driver Service**
**Timeline:** Week 5-6
**Status:** Not Started

**Goals:**
- Learn microservice patterns
- Implement service-to-service communication
- Add second microservice

**Tasks:**
- [ ] Step 3.1: Create Driver Service (registration, login, profile APIs)
- [ ] Step 3.2: Service Communication (HTTP calls, service discovery)

**Architecture Evolution:**
```
Client
  ↓
User Service (FastAPI) ←→ Driver Service (FastAPI)
  ↓                           ↓
PostgreSQL (users)      PostgreSQL (drivers)
```

---

### **PHASE 4: Introduce Kafka**
**Timeline:** Week 7-9
**Status:** Not Started

**Why Now?**
- Multiple services need to communicate
- Direct HTTP calls become complex
- Need to decouple services

**Goals:**
- Add event streaming
- Implement event-driven architecture
- Learn Kafka fundamentals

**Tasks:**
- [ ] Step 4.1: Add Kafka to Docker Compose (Zookeeper, Kafka, Kafka UI)
- [ ] Step 4.2: Create Event Schemas (UserRegistered, DriverRegistered, etc.)
- [ ] Step 4.3: Implement Event Publishing (Kafka producers)
- [ ] Step 4.4: Implement Event Consumers (analytics consumer)

**Architecture Evolution:**
```
Client
  ↓
User Service ──→ Kafka ←── Driver Service
  ↓                ↓            ↓
PostgreSQL    [Topics]    PostgreSQL
                  ↓
            Analytics Consumer
                  ↓
            PostgreSQL (analytics)
```

---

### **PHASE 5: Ride Booking Service**
**Timeline:** Week 10-12
**Status:** Not Started

**Goals:**
- Implement core business logic
- Build ride state machine
- Implement driver matching
- Event-driven ride flow

**Tasks:**
- [ ] Step 5.1: Create Ride Service (request, accept, start, complete, cancel APIs)
- [ ] Step 5.2: Ride State Machine (REQUESTED → ACCEPTED → STARTED → COMPLETED)
- [ ] Step 5.3: Event-Driven Ride Flow (RideRequested, RideAccepted, etc.)
- [ ] Step 5.4: Real-time Driver Matching (PostGIS, geospatial queries)

**Events:**
- RideRequested
- RideAccepted
- RideStarted
- RideCompleted
- RideCancelled
- DriverLocationUpdated

---

### **PHASE 6: Data Pipeline - Batch Processing**
**Timeline:** Week 13-15
**Status:** Not Started

**Goals:**
- Build analytics database
- Implement ETL pipelines
- Learn data warehousing concepts
- Add orchestration

**Tasks:**
- [ ] Step 6.1: Create Analytics Database (star schema, fact/dim tables)
- [ ] Step 6.2: Batch ETL with Python (nightly jobs, extract/transform/load)
- [ ] Step 6.3: Basic Analytics Queries (rides per day, retention, etc.)
- [ ] Step 6.4: Introduce Apache Airflow (orchestration, scheduling, monitoring)

**Analytics Schema:**
- fact_rides
- dim_users
- dim_drivers
- dim_time

---

### **PHASE 7: Introduce Spark**
**Timeline:** Week 16-18
**Status:** Not Started

**Why Now?**
- Significant data volume
- Need distributed processing
- Complex transformations required

**Goals:**
- Learn Spark fundamentals
- Implement batch processing with Spark
- Add Spark streaming

**Tasks:**
- [ ] Step 7.1: Add Spark to Docker Compose (master, worker)
- [ ] Step 7.2: Migrate Batch Jobs to PySpark (DataFrames, transformations)
- [ ] Step 7.3: Spark Streaming from Kafka (real-time aggregations)

**Architecture Evolution:**
```
Microservices → Kafka → Spark Streaming
      ↓                      ↓
Operational DBs      Analytics PostgreSQL
      ↓
Batch ETL (Spark)
      ↓
Analytics PostgreSQL
```

---

### **PHASE 8: Introduce Snowflake**
**Timeline:** Week 19-21
**Status:** Not Started

**Why Snowflake?**
- Cloud-native analytics warehouse
- Separation of storage and compute
- Time travel and data sharing
- Industry-standard tool

**Goals:**
- Set up cloud data warehouse
- Build data pipeline to Snowflake
- Create analytics dashboards

**Tasks:**
- [ ] Step 8.1: Set Up Snowflake (account, schema design)
- [ ] Step 8.2: Data Pipeline to Snowflake (Spark → S3 → Snowflake or Kafka → Snowpipe)
- [ ] Step 8.3: Analytics in Snowflake (views, dashboards, time-series analysis)

**Final Architecture:**
```
Client Apps
    ↓
API Gateway (Kong/Nginx)
    ↓
┌─────────────────────────────────┐
│   Microservices (FastAPI)       │
│  - User Service                 │
│  - Driver Service               │
│  - Ride Service                 │
└─────────────────────────────────┘
    ↓                    ↓
PostgreSQL          Kafka Cluster
(Operational)       (Event Stream)
                         ↓
                    ┌────────────┐
                    │   Spark    │
                    │ Streaming  │
                    └────────────┘
                         ↓
                    ┌────────────┐
                    │     S3     │
                    │  (Parquet) │
                    └────────────┘
                         ↓
                    ┌────────────┐
                    │ Snowflake  │
                    │ Warehouse  │
                    └────────────┘
                         ↓
                    Dashboards
```

---

## 🎓 KEY LEARNING MILESTONES

| After Phase | You Will Understand |
|-------------|---------------------|
| Phase 2 | API design, authentication, single service architecture |
| Phase 4 | Event-driven architecture, async communication |
| Phase 5 | Complex business logic in distributed systems |
| Phase 7 | Stream processing, real-time analytics |
| Phase 8 | Modern data platform architecture |

---

## 📝 IMMEDIATE NEXT STEPS (This Week)

### Priority Order:
1. ✅ Save project context (COMPLETED)
2. ⬜ Add environment configuration (.env, pydantic-settings)
3. ⬜ Implement JWT authentication (login, token generation)
4. ⬜ Add health check endpoint
5. ⬜ Add structured logging
6. ⬜ Write basic tests

---

## 🔄 PLANNED FUTURE COMPONENTS

1. Authentication system using JWT tokens
2. Protected APIs
3. User profile APIs
4. Ride booking service
5. Event publishing for ride and user events
6. Kafka event streaming
7. Spark streaming or batch processing
8. Snowflake as analytics warehouse
9. Data pipeline for ride analytics
10. Logging, monitoring, and observability
11. Service-to-service communication
12. Scalable microservice architecture

---

## 💡 IMPROVEMENTS NEEDED (Current Architecture)

1. **Environment variables** - Database credentials shouldn't be hardcoded
2. **Health check endpoints** - Add `/health` for monitoring
3. **Logging** - Structured logging from the start
4. **API versioning** - Use `/api/v1/users/register`
5. **Error handling** - Consistent error response format
6. **Tests** - Unit and integration tests
7. **Documentation** - API documentation with Swagger/OpenAPI

---

## 📚 LEARNING RESOURCES & CONCEPTS

### Key Concepts to Master:
- RESTful API design
- JWT authentication & authorization
- Microservices patterns
- Event-driven architecture
- Message queues (Kafka)
- Stream processing (Spark)
- Data warehousing (Snowflake)
- Container orchestration (Docker, Kubernetes)
- CI/CD pipelines
- Observability (logging, metrics, tracing)

---

## 🗒️ NOTES & DECISIONS

### Design Decisions:
- Using UUID for user IDs (good for distributed systems)
- Password hashing implemented (security best practice)
- Phone number as unique identifier
- Docker Compose for local development

### Future Considerations:
- API Gateway (Kong/Nginx) - Phase 5+
- Kubernetes for orchestration - Phase 8+
- Service mesh (Istio) - Advanced phase
- Monitoring (Prometheus/Grafana) - Phase 6+

---

## 📊 PROJECT METRICS

**Current Status:**
- Services: 1 (User Service)
- APIs: 1 (User Registration)
- Databases: 1 (PostgreSQL)
- Tests: 0
- Documentation: Basic README

**Target Status (End of Phase 8):**
- Services: 3+ (User, Driver, Ride)
- APIs: 15+
- Databases: 3+ (Operational, Analytics, Snowflake)
- Event Topics: 10+
- Tests: 50+
- Full documentation

---

## 🔗 REPOSITORY

**GitHub:** [Your Repository URL]
**Branch Strategy:** main (for now, will add feature branches later)

---

## 📞 CONTACT & COLLABORATION

**Developer:** Ambica
**Environment:** VS Code + Remote SSH to Cloud VM
**OS:** Windows (local), Linux (cloud VM)

---

**END OF CONTEXT DOCUMENT**

*This document will be updated after each major milestone or phase completion.*
*Use this as the single source of truth for project state and direction.*
