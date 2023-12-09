<template>
    <VApp>
        <VAppBar>header</VAppBar>
        <VMain v-bind="$attrs">
            <slot />
        </VMain>
    </VApp>
</template>
