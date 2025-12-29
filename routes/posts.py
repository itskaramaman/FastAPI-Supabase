from fastapi import APIRouter, status, HTTPException
from schemas import CreatePost
from supabase_client import supabase

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", status_code=status.HTTP_200_OK)
def get_posts():
    posts = supabase.table("posts").select("*").execute()
    return posts


@router.post("", status_code=status.HTTP_201_CREATED)
def create_new_post(post: CreatePost):
    try:
        new_post = supabase.table("posts").insert({"title": post.title, "description": post.description}).execute()
        return new_post
    except Exception:
        raise HTTPException(status_code=400, detail="Could not create Post")
    