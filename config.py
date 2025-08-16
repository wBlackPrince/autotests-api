from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Self


class HttpClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)

class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )
    test_data: TestDataConfig
    http_client: HttpClientConfig
    allure_results_dir: DirectoryPath = DirectoryPath("allure-results")

    @classmethod
    def initialize(cls) -> Self:
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)

        return Settings(allure_results_dir=allure_results_dir)

settings = Settings.initialize()
print(settings)