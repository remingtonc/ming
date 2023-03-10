(function() {
    const editor = new Editor({
        element: document.querySelector('div#editor'),
        extensions: [
            StarterKit,
        ],
        content: "<p>Let's get started!</p>",
    })

    const tiptap_plugin_buttons = {
        bold: {
            text: 'Bold',
            listener_action: () => {editor.chain().focus().toggleBold().run()}
        },
        italic: {
            text: 'Italic',
            listener_action: () => {editor.chain().focus().toggleItalic().run()}
        },
        strike: {
            text: 'Strike',
            listener_action: () => {editor.chain().focus().toggleStrike().run()}
        },
        code: {
            text: 'Code',
            listener_action: () => {editor.chain().focus().toggleCode().run()}
        },
        clear_marks: {
            text: 'Clear Marks',
            listener_action: () => {editor.chain().focus().unsetAllMarks().run()}
        },
        clear_nodes: {
            text: 'Clear Nodes',
            listener_action: () => {editor.chain().focus().clearNodes().run()}
        },
        paragraph: {
            text: 'Paragraph',
            listener_action: () => {editor.chain().focus().toggleClearNodes().run()}
        },
        h1: {
            text: 'h1',
            listener_action: () => {editor.chain().focus().toggleHeading({level: 1}).run()}
        },
        h2: {
            text: 'h2',
            listener_action: () => {editor.chain().focus().toggleHeading({level: 2}).run()}
        },
        h3: {
            text: 'h3',
            listener_action: () => {editor.chain().focus().toggleHeading({level: 3}).run()}
        },
        h4: {
            text: 'h4',
            listener_action: () => {editor.chain().focus().toggleHeading({level: 4}).run()}
        },
        bullet_list: {
            text: 'Bullet List',
            listener_action: () => {editor.chain().focus().toggleBulletList().run()}
        },
        ordered_list: {
            text: 'Ordered List',
            listener_action: () => {editor.chain().focus().toggleBulletList().run()}
        },
        code_block: {
            text: 'Code Block',
            listener_action: () => {editor.chain().focus().toggleCodeBlock().run()}
        },
        blockquote: {
            text: 'Blockquote',
            listener_action: () => {editor.chain().focus().toggleBlockquote().run()}
        },
        horizontal_rule: {
            text: 'Horizontal Rule',
            listener_action: () => {editor.chain().focus().setHorizontalRule().run()}
        },
        hard_break: {
            text: 'Hard Break',
            listener_action: () => {editor.chain().focus().setHardBreak().run()}
        },
        undo: {
            text: 'Undo',
            listener_action: () => {editor.chain().focus().undo().run()}
        },
        redo: {
            text: 'Redo',
            listener_action: () => {editor.chain().focus().redo().run()}
        },
    }

    let tiptap_toolbar = document.querySelector('div#editor-toolbar')

    for (const [key, value] of Object.entries(tiptap_plugin_buttons)) {
        let button_element = document.createElement('button')
        button_element.classList.add(
                'bg-sky-500',
                'hover:bg-sky-700',
                'text-white',
                'font-bold',
                'text-xs',
                'rounded'
        )
        button_element.textContent = value.text
        button_element.onclick = value.listener_action
        tiptap_toolbar.appendChild(button_element)
    }
})()