import DButton from "./DButton.vue"

export default {
  title: "Components/App/Atoms/DButton",
  component: DButton,
}

const Template = (args) => ({
  components: { DButton },
  setup() {
    return { args }
  },
  template: `<DButton v-bind="args">${args.default}</DButton>`,
})

export const Default = Template.bind({})
Default.args = {
  default: "Hello world!",
}

export const Block = Template.bind({})
Block.args = {
  ...Default.args,
  block: true,
}
