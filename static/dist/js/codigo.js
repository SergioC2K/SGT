const container = document.getElementById("container");
const rect = container.getBoundingClientRect();
const boxes = Array.from(container.getElementsByClassName("box"));
const filter = "selectable";

/* INIT SELECTABLE */
const selectable = new Selectable({
    filter: ".box",
    appendTo: container,
    autoScroll: {
        increment: 15,
        threshold: 0
    },
    lasso: {
        border: "2px dashed rgba(255,255,255,0.22)",
        borderRadius: "10px",
        backgroundColor: "rgba(226,226,226,0.22)"
    }
});

selectable.on("init", () => {
    boxes.forEach(box => box.classList.add("ui-selectable"));
    setThreshold();
});

/* DEMO STUFF */

init();

function init() {

    const gui = new dat.GUI();


    const tolerance = {
        name: "tolerance",
        touch: true,
        fit: false
    };

    const direction = {
        name: "shiftDirection",
        normal: true,
        reverse: false
    };

    const lassoSelect = {
        name: "lassoSelect",
        normal: true,
        sequential: false
    };

    const Filter = {
        enabled: false
    };

    const Misc = {
        type: "fixed",
        fixed: function () {
            boxes.forEach(el => {
                el.classList.remove("floated");
                el.style.position = "";
                el.style.top = "";
                el.style.left = "";
                el.style.transform = "";
            });

            selectable.update();
        },
        transformed: function () {

            const w = window.innerWidth;
            const h = window.innerHeight;
            const o = 200;
            const t = 250;
            const m = 5;

            toggle(lassoSelect, "normal");

            boxes.forEach(el => {

                const r = el.getBoundingClientRect();
                const x = getRandomInt(o, w - o);
                const y = getRandomInt(o, h - o);
                const a = getRandomInt(0, 270);
                const s = getRandomInt(-8, 15) / 10;

                el.classList.add("floated");

                el.style.position = `absolute`;
                el.style.top = `${y - rect.top}px`;
                el.style.left = `${x - rect.left}px`;

                el.style.transform = `translate3d(${getRandomInt(-50, 50)}px, ${getRandomInt(-50, 50)}px, 0) rotate(${a}deg) scale(${s})`;
            });

            selectable.update();
        },
        random: function () {
            const w = window.innerWidth;
            const h = window.innerHeight;
            const o = 200;
            const t = 250;
            const m = 5;

            toggle(lassoSelect, "normal");

            boxes.forEach(el => {

                const r = el.getBoundingClientRect();
                const x = getRandomInt(o, w - o);
                const y = getRandomInt(o, h - o);

                el.classList.add("floated");

                el.style.position = `absolute`;
                el.style.top = `${y - rect.top}px`;
                el.style.left = `${x - rect.left}px`;

                el.style.transform = `translate3d(${r.left - x - m}px, ${r.top - y - m}px, 0)`;

                el.offsetTop;

                el.style.transform = `translate3d(0px, 0px, 0)`;
                el.style.transition = `transform ${t}ms`;

                setTimeout(() => {
                    el.style.transform = "";
                    el.style.transition = "";
                }, t);
            });

            setTimeout(() => {
                selectable.update();
            }, 2000);
        }
    };

    const select = {
        selectAll: selectable.selectAll.bind(selectable),
        clear: selectable.clear.bind(selectable),
        invert: selectable.invert.bind(selectable),
        getItems: function () {
            console.log(selectable.getItems());
        },
        getNodes: function () {
            console.log(selectable.getNodes());
        },
        getSelectedItems: function () {
            console.log(selectable.getSelectedItems());
        },
        getSelectedNodes: function () {
            console.log(selectable.getSelectedNodes());
        },
    };

    const autoScroll = {
        enabled: true
    };

    const arr = [];

    const a = gui.addFolder("Methods");
    const enable = a.add(selectable, "enable");
    const disable = a.add(selectable, "disable");

    enable.onChange(() => {
        toggleView();
    });

    disable.onChange(() => {
        toggleView();
    });

    toggleItem(enable, !selectable.enabled);

    arr.push(a.add(select, "selectAll"));
    arr.push(a.add(select, "invert"));
    arr.push(a.add(select, "clear"));
    arr.push(a.add(select, "getItems"));
    arr.push(a.add(select, "getNodes"));
    arr.push(a.add(select, "getSelectedItems"));
    arr.push(a.add(select, "getSelectedNodes"));
    a.open();

    const auto = gui.addFolder("Autoscroll");
    const autoSettings = selectable.config.autoScroll;
    const autoThreshold = auto.add(selectable.config.autoScroll, "threshold").name("threshold (px)").min(-50).step(1).max(50).onChange(val => {
        selectable.config.autoScroll.threshold = val;
        autoSettings.threshold = val;
        setThreshold();
    });
    const autoToggle = auto.add(autoScroll, 'enabled').name("Enabled").onChange((bool) => {

        if (bool) {
            selectable.config.autoScroll = autoSettings;
        } else {
            selectable.config.autoScroll = bool;
        }

        toggleItem(autoThreshold, bool);


        selectable.disable();

        setTimeout(() => {
            setThreshold(!bool);
            selectable.enable();
        }, 30);
    });


    arr.push(autoToggle);

    arr.push(autoThreshold);

    autoToggle.__li.parentNode.appendChild(autoThreshold.__li);

    auto.open();


    const b = gui.addFolder("Tolerance");
    arr.push(b.add(tolerance, 'touch').listen().onChange(() => {
        toggle(tolerance, "touch")
    }));
    arr.push(b.add(tolerance, 'fit').listen().onChange(() => {
        toggle(tolerance, "fit")
    }));
    b.open();

    const b1 = gui.addFolder("lassoSelect");
    arr.push(b1.add(lassoSelect, 'normal').listen().onChange(function (bool) {
        toggle(lassoSelect, "normal")
    }));
    arr.push(b1.add(lassoSelect, 'sequential').listen().onChange(function (bool) {
        toggle(lassoSelect, "sequential")
    }));
    b1.open();

    const m = gui.addFolder("Toggle");

    arr.push(m.add(selectable.config, 'toggle').name("Enabled").onChange((bool) => {
        selectable.clear();
        selectable.container.classList.toggle(selectable.config.classes.multiple, bool);
    }));

    function toggle(obj, prop) {

        for (let param in obj) {
            if (typeof obj[param] !== "string")
                obj[param] = false;
        }
        obj[prop] = true;

        selectable.config[obj.name] = prop;
        selectable.update();
    }

    const c = gui.addFolder("Non-selectable Items");
    arr.push(c.add(Filter, 'enabled').onChange(function (bool) {
        toggleFilter(bool)
    }));

    const d = gui.addFolder("Item Positioning");
    arr.push(d.add(Misc, "random").onChange(toggleContainer));
    arr.push(d.add(Misc, "fixed").onChange(toggleContainer));
    arr.push(d.add(Misc, "transformed").onChange(toggleContainer));
    d.open();

    function toggleContainer(bool) {
        const rand = this.property === "random" || this.property === "transformed";
        container.classList.toggle("random", rand);
        selectable.setContainer(rand ? document.body : container);

        boxes.forEach(box => {
            selectable.add(box);
            box.style.opacity = 1;
        });
        selectable.lasso.style.borderColor = selectable.config.lasso.borderColor;
        selectable.lasso.style.backgroundColor = selectable.config.lasso.backgroundColor;

        if (rand) {
            selectable.lasso.style.borderColor = `rgba(0, 0, 0, 1)`;
            selectable.lasso.style.backgroundColor = `rgba(255, 255, 255, 0.2)`;
            new Set(
                Array
                    .from({
                        length: boxes.length
                    }, () => Math.floor(Math.random() * boxes.length)))
                .forEach(n => {
                    selectable.remove(boxes[n]);
                    boxes[n].style.opacity = 0;
                });
        }

        setTimeout(function () {
            selectable.update();
        }, 500);
    }


    const colors = {
        borderColor: selectable.config.lasso.borderColor.replace(/rgba\((.+)\)/, "$1").split(","),
        backgroundColor: selectable.config.lasso.backgroundColor.replace(/rgba\((.+)\)/, "$1").split(",")
    };

    const e = gui.addFolder("Lasso Styling");
    e.addColor(colors, 'borderColor').onFinishChange((a) => {
        selectable.lasso.style.borderColor = `rgba(${a.join(",")})`;
    });
    e.addColor(colors, 'backgroundColor').onFinishChange((a) => {
        selectable.lasso.style.backgroundColor = `rgba(${a.join(",")})`;
    });


    function toggleView(bool) {
        toggleItem(enable, selectable.enabled);
        toggleItem(disable, !selectable.enabled);

        arr.forEach(item => {
            toggleItem(item, !selectable.enabled);
        })
    }

    function toggleItem(item, bool) {
        item.__li.style.pointerEvents = bool ? "" : "none"
        item.__li.firstElementChild.style.opacity = bool ? 1 : .2
    }
}

function toggleFilter(bool) {
    selectable.clear();
    if (bool) {
        // Use Set to ensure unique indexes
        new Set(
            Array
                .from({
                    length: boxes.length
                }, () => Math.floor(Math.random() * boxes.length)))
            .forEach(n => selectable.remove(boxes[n]));
    } else {
        boxes.forEach(box => selectable.add(box))
    }
    selectable.update();
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

function setThreshold(bool) {
    const els = Array.from(document.getElementById("threshold").children);

    if (bool) {
        els[0].parentNode.style.display = "none";
    } else {
        els[0].parentNode.style.display = "block";
        els[0].style.top = `${selectable.config.autoScroll.threshold}px`;
        els[1].style.bottom = `${selectable.config.autoScroll.threshold}px`;
    }
}

for (var i = 0; i < cajas.length; i++) {
    var oelo = cajas[i].innerHTML;
    console.log(oelo[i])
}