import asyncio
import aiohttp

from loader import BASE_DIR
from data.config import RAPIDAPI_KEY, RAPIDAPI_HOST, RAPIDAPI_URL


class Colorizer:
    def __init_(self):
        self._result_dir = None

    @staticmethod
    async def api_request(multipart_data, headers):
        async with aiohttp.ClientSession() as session:
            async with session.post(RAPIDAPI_URL, headers=headers, data=multipart_data) as response:
                response.raise_for_status()
                return await response.read()

    async def colorize_image(self, name):
        file_path = BASE_DIR / f"images/downloads/{name}.jpg"
        with open(file_path, "rb") as f:
            file_data = f.read()

        multipart_data = aiohttp.FormData()
        multipart_data.add_field(
            "image", file_data, filename=f"{name}.jpg", content_type="image/jpeg")
        multipart_data.add_field("renderFactor", "25")

        headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": RAPIDAPI_HOST
        }

        response = await Colorizer.api_request(multipart_data, headers)

        self._result_dir = BASE_DIR / f"images/uploads/{name}_result.jpg"
        with open(self._result_dir, "wb") as f:
            f.write(response)

    @property
    def photo_dir(self):
        return self._result_dir
