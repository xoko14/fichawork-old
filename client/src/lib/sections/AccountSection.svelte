<script lang="ts">
    import { currentUser, token, activeSection} from "./../../store";

    import { onMount } from "svelte";

    import { ApiClient } from "./../../api/apiClient";
    import type { User } from "./../../api/models/User";
    import { Section } from "../Sections";

    let strtoken: string;

    token.subscribe((val) => {strtoken = val})

    //onMount(async () =>
        new ApiClient(strtoken)
            .getCurrentUser()
            .then((user) => currentUser.set(user))
    //);

</script>

<div class="section">
    <p class="m-auto">Account section</p>
    <p>{$currentUser.name}</p>

    <p><button on:click={() => {token.set(""); activeSection.set(Section.LOGIN)}}>Log out</button></p>
</div>
