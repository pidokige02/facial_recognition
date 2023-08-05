let DEBUG = true;
let host = "http://127.0.0.1:8000";

if (!DEBUG) {
  host = "https://domain.com";
}

export const APIEndpoint = `${host}/api`;

export const fileUploadURL = `${APIEndpoint}/demo/`;
export const facialRecognitionURL = `${APIEndpoint}/upload/`;
export const changeEmailURL = `${APIEndpoint}/change-email/`;