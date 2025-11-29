{{# Task 2 —› Async Data Fetcher with Retry

---

## Step One — Every Search I Made

- [https://stackoverflow.com/questions/46175660/fetch-retry-request-on-failure](https://stackoverflow.com/questions/46175660/fetch-retry-request-on-failure)
- [https://courses.bigbinaryacademy.com/learn-javascript/exercises-set-11/fetch-data-with-retry/](https://courses.bigbinaryacademy.com/learn-javascript/exercises-set-11/fetch-data-with-retry/)
- [https://dev.to/ycmjason/javascript-fetch-retry-upon-failure-3p6g](https://dev.to/ycmjason/javascript-fetch-retry-upon-failure-3p6g)
- [https://techblitz.dev/question/retry-fetch-request-error-handling-javascript](https://techblitz.dev/question/retry-fetch-request-error-handling-javascript)
- Search terms used: "javascript fetch retry", "fetch retry async await", "javascript sleep promise retry", "fetch retry loop vs recursion"

---

## Step Two — My Thought Process

While exploring, I saw a few ways to handle retries: **recursion, loop-based retry, and libraries**. I decided on a **clean loop-based async/await approach** because it’s easy to read, debug, and doesn’t need extra dependencies.

### Key Points

1. Respect async flow — avoid multiple simultaneous fetches.
2. Retry count (`maxRetries`) and delay configurable.
3. Wait 1 second between retries to avoid hammering the server.
4. Proper error propagation after all retries fail.

### Alternatives Considered

- Recursive retry — elegant but got messy with promise chains.
- External libraries (e.g., `p-retry`) — fine, but overkill for this small task.

---

## Step Three — Step-by-Step Solution Process

**1️⃣ Create a mock API**
Simulate unreliable network with a random success/failure generator:

```javascript
async function mockFetch(url) {
  return new Promise((resolve, reject) => {
    const success = Math.random() > 0.3; // 70% success rate
    setTimeout(() => {
      if (success) resolve({ data: `Fetched data from ${url}` });
      else reject(new Error("Network error"));
    }, 300);
  });
}
```

**Commit:** `feat: add mockFetch function to simulate API with random failures`

---

**2️⃣ Implement sleep helper**
Pause execution between retries:

```javascript
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
```

**Commit:** `feat: implement sleep function for retry delay`

---

**3️⃣ Implement main fetchWithRetry function**

```javascript
async function fetchWithRetry(url, maxRetries = 3) {
  let attempt = 0;

  while (attempt < maxRetries) {
    try {
      console.log(`Attempt ${attempt + 1} to fetch ${url}`);
      const result = await mockFetch(url);
      return result; // Success
    } catch (error) {
      attempt++;
      console.warn(`Attempt ${attempt} failed: ${error.message}`);
      if (attempt === maxRetries) {
        throw new Error(
          `Failed to fetch data from ${url} after ${maxRetries} attempts`
        );
      }
      await sleep(1000); // wait 1 second before retrying
    }
  }
}
```

**Commit:** `feat: implement fetchWithRetry with async/await and retry logic`

---

**4️⃣ Test the function**

```javascript
(async () => {
  try {
    const data = await fetchWithRetry("https://example.com/data", 3);
    console.log("Success:", data);
  } catch (err) {
    console.error("Final error:", err.message);
  }
})();
```

**Commit:** `test: validate fetchWithRetry with mock API`

### Problems Faced

- Recursive retry made promise chains confusing
- Needed `sleep` wrapper for retry delays
- Ensuring final error propagates after all retries failed

---

## Step Four — Why My Solution Is Best

- Simple, human-readable **loop-based async/await**
- Configurable retry count and delay
- Correct handling of asynchronous fetch and retry delays
- Clear console logging for each attempt
- Lightweight — no external libraries
- Works reliably with a mock API simulating random failures

✨ Clean, readable, and totally Ayana-approved 💡
}}
