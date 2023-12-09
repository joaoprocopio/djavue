<template>
    <VApp>
        <VAppBar>
            <template #prepend>
                <VIcon>hub</VIcon>
            </template>
        </VAppBar>
        <VMain v-bind="$attrs">
            <slot />
        </VMain>
    </VApp>
</template>
