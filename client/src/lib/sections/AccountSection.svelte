<script lang="ts">
    import { currentUser, endpoint } from "./../../store";

    import { onMount } from "svelte";
    import { get } from "svelte/store";

    import { ApiClient } from "./../../api/apiClient";
    import type { User } from "./../../api/models/User";
    let client: ApiClient;

    onMount(async () =>
        new ApiClient(get(endpoint))
            .getCurrentUser()
            .then((user) => currentUser.set(user))
    );

</script>

<div class="section">
    <p class="m-auto">Account section</p>
    <p>{$currentUser.name}</p>
</div>
