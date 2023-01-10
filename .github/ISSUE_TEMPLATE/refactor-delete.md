---
name: Refactor Delete
about: 'For Milestone #13'
title: Refactor Delete Request for Default_Recipe
labels: ''
assignees: Massacre-Saint

---

Refactor associated delete request from all promises.
## React Code

Let’s add a “Delete” button to the event and game lists.

1. Add a “Delete” button inside the `events` and `games` map in each list component
2. Create a `deleteGame` and `deleteEvent` function that takes an id parameter and makes a fetch call for a `DELETE` request to the right resource. The `id` parameter from the function should be used in the fetch url.
3. `onClick` of the button should call the `DELETE` fetch function and pass in the object’s id. After the `DELETE` function runs, then the component should get the list again and update the state.
4. Try it out in the browser to see if the delete button works and the list updates.
