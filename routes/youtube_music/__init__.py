import logging
from .wrapper import Wrapper
from fastapi import APIRouter, Depends, Request

logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/youtube_music",
    tags=["Youtube Music"],
    responses={404: {"description": "Not found"}},
)
wrapper = Wrapper()
#TODO: Add routes & make wrapper