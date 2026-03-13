# TAXI BOOKING EVENT PLATFORM - PROJECT CONTEXT

**Last Updated:** 2024-01-XX
**Current Phase:** Phase 1 - Foundation Solidification (In Progress)
**Current Step:** Step 1.2 - API Design Improvements
**Next Steps:** Health Check Endpoint, Structured Logging, JWT Authentication

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
- [x] Step 1.1: Add Configuration Management (environment variables, pydantic-settings) ✅ COMPLETED
- [x] Step 1.1a: Enhanced Error Handling (database errors, duplicate keys, proper HTTP status codes) ✅ COMPLETED
- [x] Step 1.1b: Comprehensive Input Validation (password, phone, name with detailed error messages) ✅ COMPLETED
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
2. ✅ Add environment configuration (.env, pydantic-settings) (COMPLETED)
3. ✅ Enhanced error handling for database operations (COMPLETED)
4. ✅ Comprehensive input validation with detailed error messages (COMPLETED)
5. ⬜ Add health check endpoint
6. ⬜ Add structured logging
7. ⬜ Implement JWT authentication (login, token generation)
8. ⬜ Write basic tests

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
- APIs: 1 (User Registration with comprehensive validation)
- Databases: 1 (PostgreSQL with proper error handling)
- Tests: 0
- Documentation: Basic README + Auto-generated Swagger UI
- Configuration: Environment-based with .env files
- Error Handling: Production-ready with proper HTTP status codes
- Validation: Password (4 checks), Phone (business rules), Name (character validation)

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

---

## 🎯 COMPLETED WORK DETAILS

### ✅ Step 1.1: Configuration Management (COMPLETED)

**What was implemented:**

1. **Created `config.py`** - Centralized configuration management
   - Uses `pydantic-settings` for type-safe configuration
   - Loads from environment variables and .env file
   - Provides default values for all settings
   - Includes database URL builder property

2. **Created `.env` file** - Environment-specific configuration
   - Database credentials (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD)
   - Application settings (APP_NAME, APP_VERSION, DEBUG)
   - Server settings (SERVER_HOST, SERVER_PORT)
   - **IMPORTANT:** Never commit to Git (protected by .gitignore)

3. **Created `.env.example`** - Template for developers
   - Safe to commit to Git
   - Contains placeholder values
   - Documents all required environment variables

4. **Created `.gitignore`** - Security protection
   - Prevents .env from being committed
   - Ignores Python cache files
   - Ignores IDE and OS files

5. **Updated `database/db.py`** - Uses configuration
   - Reads credentials from settings object
   - No hardcoded values
   - Includes comprehensive documentation

6. **Updated `main.py`** - Uses configuration
   - FastAPI app configured with settings
   - Returns app version and name in root endpoint

**Files Modified:**
- `backend/user-service/requirements.txt` - Added pydantic-settings, python-dotenv
- `backend/user-service/app/config.py` - NEW FILE
- `backend/user-service/.env` - NEW FILE (not in Git)
- `backend/user-service/.env.example` - NEW FILE
- `.gitignore` - NEW FILE
- `backend/user-service/app/database/db.py` - UPDATED
- `backend/user-service/app/main.py` - UPDATED

**Benefits Achieved:**
- ✅ Credentials no longer in source code
- ✅ Easy to switch between dev/staging/production
- ✅ Follows 12-Factor App methodology
- ✅ Type-safe configuration with validation
- ✅ Ready for cloud deployment (AWS Secrets Manager, etc.)

---

### ✅ Step 1.1a: Enhanced Error Handling (COMPLETED)

**What was implemented:**

1. **Database Error Handling** in `routes/user_routes.py`
   - Catches `psycopg2.errors.UniqueViolation` for duplicate phone numbers
   - Returns HTTP 409 (Conflict) with clear error message
   - Implements transaction rollback on errors
   - Handles general database errors with HTTP 500

2. **Connection Management**
   - Uses try-except-finally pattern
   - Always closes database connections (prevents leaks)
   - Properly handles cursor cleanup
   - Implements rollback on errors

3. **Better Response Format**
   - Returns user details on successful registration
   - Includes user_id, name, email, phone in response
   - Clear error messages for all failure scenarios

4. **HTTP Status Codes**
   - 200: Success
   - 409: Duplicate phone number (Conflict)
   - 422: Validation error (handled by Pydantic)
   - 500: Internal server error

**Code Example:**
```python
try:
    cursor.execute(query, (...))
    conn.commit()
except psycopg2.errors.UniqueViolation:
    conn.rollback()
    raise HTTPException(status_code=409, detail="Phone already registered")
finally:
    cursor.close()
    conn.close()
```

**Benefits Achieved:**
- ✅ Proper HTTP status codes for different errors
- ✅ No connection leaks
- ✅ Clear error messages for users
- ✅ Transaction safety with rollback
- ✅ Production-ready error handling

---

### ✅ Step 1.1b: Comprehensive Input Validation (COMPLETED)

**What was implemented:**

1. **Enhanced Password Validation** in `schemas/user_schema.py`
   - ✅ Minimum 8 characters
   - ✅ At least one uppercase letter (A-Z)
   - ✅ At least one lowercase letter (a-z)
   - ✅ At least one digit (0-9) - **NEW**
   - ✅ At least one special character (!@#$%^&*...)
   - ✅ Shows ALL validation errors at once (not one by one)

2. **Enhanced Phone Validation**
   - ✅ Exactly 10 digits
   - ✅ Cannot start with 0 or 1 (Indian phone number rules)
   - ✅ Removes spaces and dashes automatically
   - ✅ Clear error messages

3. **Enhanced Name Validation**
   - ✅ 2-100 characters
   - ✅ Only letters and spaces allowed
   - ✅ No numbers or special characters
   - ✅ Removes extra whitespace

4. **Better Documentation**
   - Added descriptions for all fields
   - Added example values
   - Auto-generates in Swagger UI
   - Helps frontend developers

**Validation Error Examples:**
```json
// Missing uppercase, digit, and special char
{
  "detail": [
    {
      "msg": "Password must contain at least one uppercase letter (A-Z). Password must contain at least one digit (0-9). Password must contain at least one special character"
    }
  ]
}
```

**Benefits Achieved:**
- ✅ Comprehensive password security
- ✅ Domain-specific validation (Indian phone numbers)
- ✅ Better user experience (all errors shown at once)
- ✅ Data quality enforcement
- ✅ Clear, actionable error messages
- ✅ Follows OWASP security guidelines

---

## 🧪 TESTING COMPLETED

**API Endpoint Tested:** `POST /users/register`

**Test Cases Verified:**
1. ✅ Valid user registration (200 Success)
2. ✅ Duplicate phone number (409 Conflict)
3. ✅ Missing uppercase in password (422 Validation Error)
4. ✅ Missing lowercase in password (422 Validation Error)
5. ✅ Missing digit in password (422 Validation Error)
6. ✅ Missing special character in password (422 Validation Error)
7. ✅ Password too short (422 Validation Error)
8. ✅ Multiple password errors at once (422 Validation Error)
9. ✅ Invalid phone format (422 Validation Error)
10. ✅ Phone starting with 0 or 1 (422 Validation Error)
11. ✅ Invalid name with numbers (422 Validation Error)
12. ✅ Invalid email format (422 Validation Error)

**Testing Methods:**
- Swagger UI: `http://34.57.187.115:8000/docs`
- cURL commands
- Browser-based testing

**All tests passing successfully!** ✅

---

## 📁 CURRENT PROJECT STRUCTURE

```
taxi-booking-event-platform/
├── .gitignore                          # NEW - Protects secrets
├── PROJECT_CONTEXT.md                  # NEW - This file
├── README.md
├── sample.txt
├── docker-compose.yml
├── backend/
│   └── user-service/
│       ├── Dockerfile
│       ├── requirements.txt            # UPDATED - Added pydantic-settings
│       ├── .env                        # NEW - Environment variables (not in Git)
│       ├── .env.example                # NEW - Template (in Git)
│       └── app/
│           ├── main.py                 # UPDATED - Uses config
│           ├── config.py               # NEW - Configuration management
│           ├── database/
│           │   └── db.py               # UPDATED - Uses config
│           ├── routes/
│           │   └── user_routes.py      # UPDATED - Error handling
│           ├── schemas/
│           │   └── user_schema.py      # UPDATED - Enhanced validation
│           └── services/
├── database/
├── docs/
└── frontend/
```

---

## 🎓 KEY LEARNINGS & INTERVIEW TIPS

### **1. Environment Configuration**
- **Why:** Security, portability, 12-Factor App compliance
- **How:** pydantic-settings, .env files, .gitignore
- **Interview Tip:** Explain how you'd use AWS Secrets Manager in production

### **2. Error Handling**
- **Why:** Better UX, proper HTTP semantics, debugging
- **How:** try-except-finally, specific exception catching, proper status codes
- **Interview Tip:** Discuss connection pooling and circuit breakers

### **3. Input Validation**
- **Why:** Security, data quality, user experience
- **How:** Pydantic validators, regex patterns, business rules
- **Interview Tip:** Mention OWASP guidelines and password breach databases

### **4. Database Connection Management**
- **Why:** Prevent connection leaks, transaction safety
- **How:** finally blocks, rollback on errors, connection pooling
- **Interview Tip:** Discuss SQLAlchemy ORM and connection pools

### **5. API Documentation**
- **Why:** Developer experience, testing, onboarding
- **How:** FastAPI auto-generates Swagger UI from Pydantic models
- **Interview Tip:** Mention OpenAPI specification and API versioning

---

## 🚀 WHAT'S NEXT

### **Immediate Next Steps (Choose One):**

**Option A: Continue Phase 1 Improvements**
1. Add health check endpoint (`/health`, `/ready`)
2. Add structured logging (JSON format, correlation IDs)
3. Add API versioning (`/api/v1/users/register`)
4. Write unit and integration tests

**Option B: Move to Phase 2 - Authentication**
1. Implement JWT token generation
2. Add login endpoint
3. Create protected endpoints
4. Add refresh token mechanism

**Recommendation:** Complete Phase 1 improvements first for a solid foundation.

---

**END OF CONTEXT DOCUMENT**

*This document will be updated after each major milestone or phase completion.*
*Use this as the single source of truth for project state and direction.*
*Last saved: After completing environment configuration, error handling, and comprehensive validation.*
