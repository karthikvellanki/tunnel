let DEBUG = true;
let host = "http://127.0.0.1:8000";
if (DEBUG === false) {
  host = "";
}

export const APIEndpoint = `${host}/api`;

export const emailURL = `${APIEndpoint}/email/`;
export const changeEmailURL = `${APIEndpoint}/change-email/`;
export const changePasswordURL = `${APIEndpoint}/change-password/`;
export const APIkeyURL = `${APIEndpoint}/api-key/`;

export const loginURL = `${host}/rest-auth/login/`;
export const signupURL = `${host}/rest-auth/registration/`;
