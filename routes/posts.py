from fastapi import APIRouter, status, HTTPException
from schemas import PostModel
from supabase_client import supabase

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", status_code=status.HTTP_200_OK)
def get_posts():
    try:
        posts = supabase.table("posts").select("*").execute()
        return posts
    except Exception:
        raise HTTPException(status_code=400, detail="Could not fetch Post")


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_post(id: str):
    try:
        post = supabase.table("posts").select("*").eq("id", id).execute()
        if not post:
            raise HTTPException(status_code=404, detail="Post not Found")
        return post
    except Exception:
        raise HTTPException(status_code=400, detail="Could not fetch Post")


@router.post("", status_code=status.HTTP_201_CREATED)
def create_new_post(post: PostModel):
    try:
        author_id = supabase.auth.get_user().user.id
        new_post = supabase.table("posts").insert({
            "title": post.title,
            "description": post.description,
            "author_id": author_id
        }).execute()

        return new_post
    except Exception:
        raise HTTPException(status_code=400, detail="Could not create Post")
    

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_post(id: str):
    try:
        user_id = supabase.auth.get_user().user.id
        post = supabase.table("posts").select("*").eq("id", id).execute()
        print(user_id, post)
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")

        if post.data[0]['author_id'] != user_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")
        
        supabase.table("posts").delete().eq("id", id).execute()
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not Allowed")
    


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_post(id: str, post: PostModel):
    try:
        db_post = supabase.table("posts").select("*").eq("id", id).execute()

        if not db_post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")
        
        updated_post = supabase.table("posts").update({
            "title": post.title,
            "description": post.description
        }).eq("id", id).execute()

        return updated_post
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not Allowed")
