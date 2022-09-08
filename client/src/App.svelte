<script lang="ts">
  import svelteLogo from "./assets/svelte.svg";
import { Section } from "./lib/Sections";
import AccountSection from "./lib/sections/AccountSection.svelte";
  import ClockInSection from "./lib/sections/ClockInSection.svelte";
import ExportSection from "./lib/sections/ExportSection.svelte";
  import HistorySection from "./lib/sections/HistorySection.svelte";
  import Sidebar from "./lib/sidebar/Sidebar.svelte";

  export let section: Section = Section.CLOCKIN;
</script>

<main>
  <div class="flex ">
    <Sidebar bind:section/>
    {#if section == Section.CLOCKIN}
      <ClockInSection />
    {:else if section == Section.HISTORY}
      <HistorySection />
    {:else if section == Section.ACCOUNT}
      <AccountSection/>
    {:else if section == Section.EXPORT}
      <ExportSection/>
    {/if}
  </div>
</main>

<style>
</style>
