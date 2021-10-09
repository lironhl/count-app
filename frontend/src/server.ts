import { Configuration, CountApi } from "./api";

const basePath =
  process.env.NODE_ENV === "development" ? "http://localhost:8000" : "https://kks-kshishim.azurewebsites.net";
const config = new Configuration({ basePath });

export const countApi = new CountApi(config);
