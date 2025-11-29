Task 2 -Async Data Fetcher with Retry

step one
https://stackoverflow.com/questions/46175660/fetch-retry-request-on-failure
https://courses.bigbinaryacademy.com/learn-javascript/exercises-set-11/fetch-data-with-retry/

https://dev.to/ycmjason/javascript-fetch-retry-upon-failure-3p6g
https://techblitz.dev/question/retry-fetch-request-error-handling-javascript
{{# Task 2 —› Async Data Fetcher with Retry

---

## Step One — Every Search I Made

- https://stackoverflow.com/questions/46175660/fetch-retry-request-on-failure
- https://courses.bigbinaryacademy.com/learn-javascript/exercises-set-11/fetch-data-with-retry/
- https://dev.to/ycmjason/javascript-fetch-retry-upon-failure-3p6g
- https://techblitz.dev/question/retry-fetch-request-error-handling-javascript
- Search terms used: "javascript fetch retry", "fetch retry async await", "javascript sleep promise retry"

---

## Step Two — My Thought Process

When researching, I found multiple approaches: recursive retry, loop-based retry, and library-based solutions. I decided to implement a **loop-based async/await retry with a delay** because:

### Key Points

1. Must handle asynchronous fetch properly — cannot fire multiple simultaneous requests.
2. Retry count and delay must be configurable.
3. Should wait a fixed interval (1 second) between retries, avoiding server flooding.
4. Proper error propagation if all retries fail.
