# from fastapi import APIRouter

# from app.api.v1.users import router as users_router
# from app.api.v1.resumes import router as resumes_router
# from app.api.v1.companies import router as companies_router

# api_router = APIRouter()

# api_router.include_router(users_router)
# api_router.include_router(resumes_router)
# api_router.include_router(companies_router)

from fastapi import APIRouter

api_router = APIRouter()

try:
    from app.api.v1.users import router as users_router
    api_router.include_router(users_router)
    print("Users router loaded")
except Exception as e:
    print("Users router error:", repr(e))

try:
    from app.api.v1.resumes import router as resumes_router
    api_router.include_router(resumes_router)
    print("Resumes router loaded")
except Exception as e:
    print("Resumes router error:", repr(e))

try:
    from app.api.v1.companies import router as companies_router
    api_router.include_router(companies_router)
    print("Companies router loaded")
except Exception as e:
    print("Companies router error:", repr(e))

try:
    from app.api.v1.jobs import router as jobs_router
    api_router.include_router(jobs_router)
    print("Jobs router loaded")
except Exception as e:
    print("Jobs router error:", repr(e))