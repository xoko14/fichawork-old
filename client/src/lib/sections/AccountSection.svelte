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

    function logout(){
        token.set("")
        activeSection.set(Section.LOGIN)
    }

</script>

<div class="section">
    <div class="card">
        <p class="m-auto text-3xl mb-4">Hi, {$currentUser.name}</p>
        <button on:click={logout} class="button">Log out</button>
    </div>
</div>
