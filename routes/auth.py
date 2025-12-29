from fastapi import APIRouter
from schemas import UserAuth
from supabase_client import supabase

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def create_user(user: UserAuth):
    response = supabase.auth.sign_up({"email": user.email, "password": user.password})
    return response


@router.post("/login")
def sign_in(user: UserAuth):
    response = supabase.auth.sign_in_with_password({"email": user.email, "password": user.password})
    return response

@router.get("/session")
def get_session():
    return supabase.auth.get_user()