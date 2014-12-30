# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20141230125450) do

  create_table "visits", force: true do |t|
    t.string   "url"
    t.datetime "visit_at"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "title"
    t.integer  "visit_count"
    t.string   "email"
    t.string   "browser_type"
    t.string   "browser_id"
    t.string   "base_url"
  end

  add_index "visits", ["browser_type", "browser_id"], name: "index_visits_on_browser_type_and_browser_id"
  add_index "visits", ["email"], name: "index_visits_on_email"
  add_index "visits", ["url"], name: "index_visits_on_url"
  add_index "visits", ["visit_at"], name: "index_visits_on_visit_at"

end
